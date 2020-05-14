from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from .forms import RegistrationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User


# Create your views here.
# def get_absolute_url(self):
#     return reverse('user_detail', kwargs={'pk': self.pk})


class UserLoginView(LoginView):
    template_name = 'users_app/login.html'


class RegisterUserCreateView(CreateView):
    model = User
    template_name = 'users_app/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')


# ListView
class UsersListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users_app/users.html'

    def get_context_data(self, *args, **kwargs):
        """

        :param object_list:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        context['user_name'] = 'Пользователи'
        return context


# CreateView
class UserCreateView(LoginRequiredMixin, CreateView):
    fields = ('email', 'first_name', 'last_name', 'avatar')

    model = User
    success_url = reverse_lazy('users:users')
    template_name = 'users_app/create.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


# DetailView
class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'users_app/user.html'

    def test_func(self):
        return self.request.user.is_superuser


# UpdateView
class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ('email', 'first_name', 'last_name', 'avatar')

    model = User
    success_url = reverse_lazy('users:users')
    template_name = 'users_app/profile.html'


# DeleteView
class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users:users')
    template_name = 'users_app/confirm_delete.html'


# ChangePass
class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    model = User
    success_url = reverse_lazy('users:users')
    template_name = 'users_app/passchange.html'


# PasswordResetView
class UserPasswordResetView(LoginRequiredMixin, PasswordResetView):
    model = User
    success_url = reverse_lazy('users:users')
    template_name = 'users_app/passreset.html'

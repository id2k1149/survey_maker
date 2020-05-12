from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .forms import ContactForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Company


# Create your views here.
def main_view(request):
    pass
    return render(request, 'companies_app/index.html', context={})


def landing_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                'Contact message',
                f'Ваш сообщение "{subject}" принято',
                'id2k1149@gmail.com',
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect(reverse('companies:index'))

        else:
            return render(request, 'companies_app/landing.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'companies_app/landing.html', context={'form': form})


# ListView
class CompaniesListView(ListView):
    model = Company
    template_name = 'companies_app/companies.html'

    def employees_in_company(self):
        employees_list = self.employees.all()
        total_staff = len(employees_list)
        print(total_staff)
        return total_staff


# DetailView
class CompanyDetailView(UserPassesTestMixin, DetailView):
    model = Company
    template_name = 'companies_app/company.html'

    def test_func(self):
        return self.request.user.is_superuser


# CreateView
class CompanyCreateView(LoginRequiredMixin, CreateView):
    fields = ('name',)
    model = Company
    success_url = reverse_lazy('companies:companies')
    template_name = 'companies_app/create.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


# UpdateView
class CompanyUpdateView(UpdateView):
    fields = '__all__'

    model = Company
    success_url = reverse_lazy('companies:companies')
    template_name = 'companies_app/update.html'


class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('companies:companies')
    template_name = 'companies_app/confirm_delete.html'


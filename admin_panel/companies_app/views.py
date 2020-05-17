from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .forms import ContactForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Company, Department


# Create your views here.
# def main_view(request):
#     pass
#     return render(request, 'companies_app/index.html', context={})


def main_view(request):
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
            return render(request, 'companies_app/index.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'companies_app/index.html', context={'form': form})


# ListView
class CompaniesListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'companies_app/companies.html'

    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     if query:
    #         return Company.objects.filter(name=query)
    #     else:
    #         return Company.objects.all()


class CompanySearchView(ListView):
    model = Company
    template_name = 'companies_app/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Company.objects.filter(Q(name__icontains=query))
        return object_list


# DetailView with users
class CompanyDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Company
    template_name = 'companies_app/company.html'

    def test_func(self):
        return self.request.user.is_superuser


# DetailView with departments
class CompanyDepartmentsDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Company
    template_name = 'companies_app/company_structure.html'

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
class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    fields = '__all__'

    model = Company
    success_url = reverse_lazy('companies:companies')
    template_name = 'companies_app/update.html'


class CompanyDelete(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = reverse_lazy('companies:companies')
    template_name = 'companies_app/confirm_delete.html'


# CreateView
class DepartmentCreateView(LoginRequiredMixin, CreateView):
    fields = '__all__'
    model = Department
    success_url = reverse_lazy('companies:company_structure')
    template_name = 'companies_app/add_department.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # form.instance.departments_set =
        return super().form_valid(form)




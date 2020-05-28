from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .forms import ContactForm, DepartmentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Company, Department


# Create your views here.
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


class CompanySearchView(ListView):
    model = Company
    template_name = 'companies_app/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Company.objects.filter(Q(name__icontains=query))
        return object_list


# DetailView with users
class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'companies_app/company.html'


# DetailView with departments
class CompanyDepartmentsDetailView(LoginRequiredMixin,  DetailView):
    model = Company
    template_name = 'companies_app/company_structure.html'


# DetailView with add department
class AddDepartmentDetailView(LoginRequiredMixin,  DetailView):
    model = Company
    template_name = 'companies_app/company_add_department.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = Company.objects.get(name=str(*kwargs.values())).id
        context['form'] = DepartmentForm(company_id)
        return context


class AddDepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    fields = '__all__'
    template_name = 'companies_app/company_add_department.html'
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.company_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        company = get_object_or_404(Company, pk=self.company_pk)
        form.instance.company = company
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('companies:company_structure', kwargs={'pk': self.company_pk})


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

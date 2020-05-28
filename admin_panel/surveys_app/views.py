from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Survey
from .forms import StepOneForm, StepTwoForm, StepThreeForm
from formtools.wizard.views import SessionWizardView


# Create your views here.
# ListView
class SurveysListView(LoginRequiredMixin, ListView):
    model = Survey
    template_name = 'surveys_app/surveys.html'


# FormWizardView
class FormWizardView(SessionWizardView):
    template_name = "surveys_app/create.html"
    form_list = [StepOneForm, StepTwoForm, StepThreeForm]

    def done(self, form_list, **kwargs):
        # for form in self.form_list.items():
        #     form[-1].save()
        data = {k: v for form in form_list for k, v in form.cleaned_data.items()}
        Survey.objects.create(**data)
        return render(self.request, 'surveys_app/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


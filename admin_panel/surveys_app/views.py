from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Survey
from .forms import StepOneForm, StepTwoForm, StepThreeForm
from formtools.wizard.views import SessionWizardView


# Create your views here.
# def edit_survey(request, id):
#     survey = get_object_or_404(Survey, id=id)
#     return render(request, 'surveys_app/survey.html', context={'survey': survey})
#

# ListView
class SurveysListView(LoginRequiredMixin, ListView):
    model = Survey
    template_name = 'surveys_app/surveys.html'


# FormWizardView
class FormWizardView(SessionWizardView):
    template_name = "surveys_app/add_survey.html"
    form_list = [StepOneForm, StepTwoForm, StepThreeForm]

    def done(self, form_list, **kwargs):
        data = {k: v for form in form_list for k, v in form.cleaned_data.items()}
        Survey.objects.create(**data)
        # return render(self.request, 'surveys_app/done.html', {
        #     'form_data': [form.cleaned_data for form in form_list],
        # })
        return HttpResponseRedirect(reverse("surveys:surveys"))


# SurveyDetailView with departments
class SurveyDetailView(LoginRequiredMixin,  DetailView):
    model = Survey
    template_name = 'surveys_app/survey.html'




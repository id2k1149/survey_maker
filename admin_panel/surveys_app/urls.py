from django.urls import path
from surveys_app import views
from surveys_app.forms import StepOneForm, StepTwoForm, StepThreeForm

app_name = 'surveys_app'

named_contact_forms = (
    ('contactdata', StepOneForm),
    ('leavemessage', StepTwoForm),
)

urlpatterns = [
    path('surveys/', views.SurveysListView.as_view(), name='surveys'),
    path('create/', views.FormWizardView.as_view([StepOneForm,
                                                  StepTwoForm,
                                                  StepThreeForm]), name='create'),

]
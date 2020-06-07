from django.urls import path
from surveys_app import views
from surveys_app.forms import StepOneForm, StepTwoForm, StepThreeForm

app_name = 'surveys_app'

# named_contact_forms = (
#     ('contactdata', StepOneForm),
#     ('leavemessage', StepTwoForm),
# )

urlpatterns = [
    path('surveys/', views.SurveysListView.as_view(), name='surveys'),
    path('survey/<int:pk>/', views.SurveyDetailView.as_view(), name='survey'),

    path('survey_add_page/<int:pk>/', views.SurveyAddPageCreateView.as_view(), name='survey_add_page'),
    path('add_page2/<int:pk>/', views.Survey2AddPageCreateView.as_view(), name='add_page2'),
    path('add_page/<int:pk>/', views.SurveyAddPageView.as_view(), name='add_page'),
    # path('page_delete/<int:pk>/', views.page_delete, name='page_delete'),
    path('delete/<int:pk>/', views.PageDeleteView.as_view(), name='delete'),
    # path('add_question/<int:pk>/', views.SurveyAddQuestionView.as_view(), name='add_question'),
    path('hello/<int:pk>/', views.HelloUpdateView.as_view(), name='hello'),
    path('info/<int:pk>/', views.InfoUpdateView.as_view(), name='info'),
    path('bye/<int:pk>/', views.ByeUpdateView.as_view(), name='bye'),
    path('add_survey/', views.FormWizardView.as_view([StepOneForm, StepTwoForm, StepThreeForm]), name='add_survey'),



]
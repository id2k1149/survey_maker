from django.urls import path
from surveys_app import views
from surveys_app.forms import StepOneForm, StepTwoForm, StepThreeForm

app_name = 'surveys_app'

# named_contact_forms = (
#     ('contactdata', StepOneForm),
#     ('leavemessage', StepTwoForm),
# )

urlpatterns = [
    path('add_survey/', views.FormWizardView.as_view([StepOneForm, StepTwoForm, StepThreeForm]), name='add_survey'),
    path('surveys/', views.SurveysListView.as_view(), name='surveys'),
    path('survey/<int:pk>/', views.SurveyDetailView.as_view(), name='survey'),
    path('del_survey/<int:pk>/', views.SurveyDeleteView.as_view(), name='del_survey'),

    path('hello/<int:pk>/', views.HelloUpdateView.as_view(), name='hello'),
    path('info/<int:pk>/', views.InfoUpdateView.as_view(), name='info'),
    path('bye/<int:pk>/', views.ByeUpdateView.as_view(), name='bye'),
    path('upd_page/<int:pk>/', views.PageUpdateView.as_view(), name='upd_page'),
    path('page/<int:pk>/', views.PageDetailView.as_view(), name='page'),
    path('add/<int:pk>/', views.AddPageCreateView.as_view(), name='add'),
    path('del_page/<int:pk>/', views.PageDeleteView.as_view(), name='del_page'),

    path('del_question/<int:pk>/', views.QuestionDeleteView.as_view(), name='del_question'),
    path('add_question/<int:pk>/', views.PageQuestionDetailView.as_view(), name='add_question'),
    path('add_question2/<int:pk>/', views.QuestionCreateView.as_view(), name='add_question2'),
    path('upd_question/<int:pk>/', views.QuestionUpdateView.as_view(), name='upd_question'),




]
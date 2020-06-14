from django.urls import path
from surveys_app import views
from surveys_app.forms import StepOneForm, StepTwoForm, StepThreeForm

app_name = 'surveys_app'

# named_contact_forms = (
#     ('contactdata', StepOneForm),
#     ('leavemessage', StepTwoForm),
# )

urlpatterns = [
    path('', views.main_view, name='index'),

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

    path('add_question/<int:pk>/', views.PageQuestionDetailView.as_view(), name='add_question'),
    path('add_question2/<int:pk>/', views.QuestionCreateView.as_view(), name='add_question2'),
    path('upd_question/<int:pk>/', views.QuestionUpdateView.as_view(), name='upd_question'),
    path('del_question/<int:pk>/', views.QuestionDeleteView.as_view(), name='del_question'),

    path('add_answer/<int:pk>/', views.QuestionAnswerDetailView.as_view(), name='add_answer'),
    path('add_answer2/<int:pk>/', views.QuestionAnswerCreateView.as_view(), name='add_answer2'),

    path('welcome/<int:pk>/', views.SurveyWelcome.as_view(), name='welcome'),
    # path('welcome/<slug:slug>/', views.SurveyWelcome.as_view(), name='welcome'),
    path('instruction/<int:pk>/', views.SurveyInstruction.as_view(), name='instruction'),
    path('see_you_later/<int:pk>/', views.SurveySeeYouLater.as_view(), name='see_you_later'),
    path('pages/<survey_id>', views.SurveyPagesListViewDemo.as_view(), name='pages'),
    path('create/', views.create_respond, name='create'),
    path('pages_d/<int:pk>/', views.PageResponseDetailView.as_view(), name='pages_d'),
    path('pages_d2/<int:pk>/', views.ResponseCreateView.as_view(), name='pages_d2'),
    path('pages_d3/<int:pk>/', views.StartSurveyCreateView.as_view(), name='pages_d3'),

]

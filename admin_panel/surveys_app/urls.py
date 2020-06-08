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
    path('edit_page/<int:pk>/', views.SurveyUpdatePageUpdateView.as_view(), name='edit_page'),
    path('add/<int:pk>/', views.AddPageCreateView.as_view(), name='add'),
    # path('edit_page/<int:pk>/', views.SurveyUpdatePageView.as_view(), name='edit_page'),
    path('del_page/<int:pk>/', views.PageDeleteView.as_view(), name='del_page'),
    path('del_survey/<int:pk>/', views.SurveyDeleteView.as_view(), name='del_survey'),
    path('hello/<int:pk>/', views.HelloUpdateView.as_view(), name='hello'),
    path('info/<int:pk>/', views.InfoUpdateView.as_view(), name='info'),
    path('bye/<int:pk>/', views.ByeUpdateView.as_view(), name='bye'),
    path('add_survey/', views.FormWizardView.as_view([StepOneForm, StepTwoForm, StepThreeForm]), name='add_survey'),



]
from django.urls import path
from quiz_app import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'quiz_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='detail'),
    path('<int:poll_id>/vote/', csrf_exempt(views.vote), name='vote'),
    path('<int:pk>)/results/', csrf_exempt(views.ResultsView.as_view()), name='results'),


]


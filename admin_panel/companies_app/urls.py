from django.urls import path
from companies_app import views

app_name = 'companies_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('landing/', views.landing_view, name='landing'),
    path('companies/', views.CompaniesListView.as_view(), name='companies'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company'),
    path('create/', views.CompanyCreateView.as_view(), name='create'),


]
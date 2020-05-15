from django.urls import path
from companies_app import views

app_name = 'companies_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    # path('landing/', views.landing_view, name='landing'),
    path('companies/', views.CompaniesListView.as_view(), name='companies'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company'),
    path('create/', views.CompanyCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.CompanyUpdateView.as_view(), name='update'),
    path('confirm_delete/<int:pk>/', views.CompanyDelete.as_view(), name='confirm_delete'),
    # path('structure/<int:pk>/', views.StructureDetailView.as_view(), name='structure'),
    # path('structure/<int:id>/', views.show_structure, name='structure'),
    path('structure/', views.show_structure, name='structure'),


]


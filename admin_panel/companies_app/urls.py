from django.urls import path
from companies_app import views

app_name = 'companies_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    # path('landing/', views.landing_view, name='landing'),
    path('companies/', views.CompaniesListView.as_view(), name='companies'),
    path('search/', views.CompanySearchView.as_view(), name='search_results'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company'),
    path('company_structure/<int:pk>/', views.CompanyDepartmentsDetailView.as_view(), name='company_structure'),
    path('company_surveys/<int:pk>/', views.CompanySurveysDetailView.as_view(), name='company_surveys'),
    path('company_add_department/<int:pk>/', views.AddDepartmentDetailView.as_view(), name='company_add_department'),
    path('add_department/<int:pk>/', views.AddDepartmentCreateView.as_view(), name='add_department'),
    path('create/', views.CompanyCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.CompanyUpdateView.as_view(), name='update'),
    path('confirm_delete/<int:pk>/', views.CompanyDelete.as_view(), name='confirm_delete'),
    # path('add_department/', views.DepartmentCreateView.as_view(), name='add_department'),
    # path('structure/<int:pk>/', views.StructureDetailView.as_view(), name='structure'),
    # path('structure/<int:id>/', views.show_structure, name='structure'),
    # path('structure/', views.show_structure, name='structure'),
    # path('departments/', views.DepartmentsListView.as_view(), name='departments'),


]


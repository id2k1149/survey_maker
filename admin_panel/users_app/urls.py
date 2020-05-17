from django.urls import path
from users_app import views
from django.contrib.auth.views import LogoutView


app_name = 'users_app'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.RegisterUserCreateView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', views.UsersListView.as_view(), name='users'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user'),
    path('profile/<int:pk>/', views.UserUpdateView.as_view(), name='profile'),
    path('confirm_delete/<int:pk>/', views.UserDelete.as_view(), name='confirm_delete'),
    path('passchange/<int:pk>/', views.UserPasswordChangeView.as_view(), name='passchange'),
    path('passreset/<int:pk>/', views.UserPasswordResetView.as_view(), name='passreset'),

    ]

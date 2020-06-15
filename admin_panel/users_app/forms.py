from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'placeholder': 'bruce@wayne.com',
                                                           'class': "form-control rounded-0"}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.TextInput(attrs={'placeholder': 'At least 8 characters',
                                                              'class': "form-control rounded-0"}))
    password2 = forms.CharField(label='Подтвердить пароль',
                                widget=forms.TextInput(attrs={'class': "form-control rounded-0"}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
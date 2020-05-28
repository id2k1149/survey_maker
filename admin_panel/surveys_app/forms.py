from django import forms
from companies_app.models import Company
from .models import Survey


class StepOneForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
                               attrs={'placeholder': 'Введите название опроса',
                                      'class': 'form-control'}))


class StepTwoForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()


class StepThreeForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['company', ]



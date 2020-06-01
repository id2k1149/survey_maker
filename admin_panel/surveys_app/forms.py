from django import forms
from .models import Survey


class StepOneForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите название опроса',
                                                         'class': 'form-control'}))


class StepTwoForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
    # start_date = forms.DateField(widget=forms.TextInput(attrs=
    # {
    #     'class': 'datepicker'
    # }))
    # end_date = forms.DateField(widget=forms.TextInput(attrs=
    # {
    #     'class': 'datepicker'
    # }))


class StepThreeForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['company', ]


# class HelloForm(forms.ModelForm):
#     hello_title = forms.CharField(label='ЗАГОЛОВОК',
#                                   widget=forms.TextInput(attrs={'class': "form-control rounded-0"}))
#
#     hello_text = forms.CharField(label='ТЕКСТ',
#                                  widget=forms.Textarea(attrs={'class': "form-control rounded-0"}))
#
#     class Meta:
#         model = Survey
#         fields = ['hello_title', 'hello_text', ]











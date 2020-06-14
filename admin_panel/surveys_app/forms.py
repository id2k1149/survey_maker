from django import forms
from .models import Survey, Pages, Question, Answer, MonoResponse


class ContactForm(forms.Form):
    email = forms.EmailField(label='email',
                             widget=forms.TextInput(attrs={'class': "form-control rounded-0"}))
    message = forms.CharField(label='Сообщение',
                              widget=forms.Textarea(attrs={'placeholder': 'Напишите здесь...',
                                                           'class': "form-control rounded-0"}))


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


class PageForm(forms.ModelForm):

    # page_name = forms.CharField(label='ЗАГОЛОВОК',
    #                             widget=forms.TextInput(attrs={'class': "form-control rounded-0"}))
    #
    # page_help = forms.CharField(label='ПОМОЩЬ',
    #                             widget=forms.Textarea(attrs={'class': "form-control rounded-0"}))

    class Meta:
        model = Pages
        fields = ['page_name', 'page_help', ]


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        exclude = ('page', 'parent', 'image',)


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['name', ]


class ResponseForm(forms.ModelForm):
    # def __init__(self, q_id, *args, **kwargs):
    #     super(ResponseForm, self).__init__(*args, **kwargs)
    #     # self.fields['answer'].queryset = Answer.objects.filter(question=q_id)
    #     # print(self.fields['answer'].queryset)
    #     print(q_id)

    answer = forms.ModelMultipleChoiceField(queryset=Answer.objects.all(),
                                            widget=forms.CheckboxSelectMultiple())

    # answer = forms.ModelChoiceField(queryset=Answer.objects.all(),
    #                                 widget=forms.CheckboxInput)

    class Meta:
        model = MonoResponse
        fields = ['answer', ]


class PageForm2(forms.ModelForm):

    class Meta:
        model = Pages
        fields = []

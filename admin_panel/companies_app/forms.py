from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя',
                           widget=forms.TextInput(attrs={'class': "form-control rounded-0"}))
    email = forms.EmailField(label='email',
                             widget=forms.TextInput(attrs={'class': "form-control rounded-0"}))
    subject = forms.CharField(label='Тема',
                              widget=forms.TextInput(attrs={'class': "form-control rounded-0"}))
    message = forms.CharField(label='Сообщение',
                              widget=forms.Textarea(attrs={'placeholder': 'Напишите здесь...',
                                                           'class': "form-control rounded-0"}))



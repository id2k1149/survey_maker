from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):
    def __init__(self, new_id, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Department.objects.all().filter(company=new_id)

    department_name = forms.CharField(label='Название',
                                      widget=forms.TextInput(
                                          attrs={'placeholder': 'Name', 'class': 'form-control rounded-0'}))

    class Meta:
        model = Department
        exclude = ('company',)

from .models import Department
from django import forms

class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['school','name','year']
        
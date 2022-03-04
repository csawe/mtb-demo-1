from .models import Unit
from django import forms

class UnitModelForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_code', 'unit_name', 'lecturer']
        
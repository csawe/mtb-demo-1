from django import forms
from .models import Unit

class UnitModelForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_code', 'unit_name', 'lecturer']
        
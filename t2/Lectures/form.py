from time import time
from django import forms

from Users.models import NewUser
from .models import Lecture

class LectureModelForm(forms.ModelForm):
    lecturer = NewUser.objects.filter(group='lecturer')
    class Meta:
        model = Lecture
        fields = ['unit', 'lecturer', 'department', 'room', 'day', 'start_time', 'duration']
        widgets = {
            'start_time': forms.TimeInput(attrs={"type":"time"})
        }
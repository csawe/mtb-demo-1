from django import forms
from .models import Room
from Lectures.views import timestamps

class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_id', 'room_location', 'room_carrying_capacity']
        
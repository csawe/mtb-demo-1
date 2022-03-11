from django import forms
from .models import Room

class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_id', 'room_location', 'room_carrying_capacity', 'functioning_electrical_sockets', 'ethernet_ports']
        
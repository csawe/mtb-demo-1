from django.urls import path
from .views import room_list_view, room_create_view, RoomUpdateView

app_name = 'Rooms'

urlpatterns = [
    path('', room_list_view, name='room-list-view'),
    path('create/', room_create_view, name='room-create-view'),
    path('update/<int:id>', RoomUpdateView.as_view(), name='room-update-view'),
]

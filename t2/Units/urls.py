from django.urls import path
from .views import unit_list_view, unit_create_view, UnitUpdateView

app_name = 'Units'

urlpatterns = [
    path('', unit_list_view, name='unit-list-view'),
    path('create/', unit_create_view, name='unit-create-view'),
    path('update/<int:id>', UnitUpdateView.as_view(), name='unit-update-view'),
]

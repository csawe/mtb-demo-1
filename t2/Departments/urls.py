from django.urls import path
from .views import department_list_view, department_create_view, DepartmentUpdateView

app_name = 'Departments'

urlpatterns = [
    path('', department_list_view, name='department-list-view'),
    path('create', department_create_view, name='department-create-view'),
    path('update/<int:id>', DepartmentUpdateView.as_view(), name='deparment-update-view'),
]

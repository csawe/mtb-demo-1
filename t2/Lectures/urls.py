from django.urls import path
from .views import lecture_list_view, lecture_create_view, LectureUpdateView, lecture_student_view

app_name = 'Lectures'

urlpatterns = [
    path('master/', lecture_list_view, name='lecture-list-view'),
    path('create', lecture_create_view, name='lecture-create-view'),
    path('update/<int:id>', LectureUpdateView.as_view(), name='lecture-update-view'),
    path('',lecture_student_view, name='lecture-student-view')
]

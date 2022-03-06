from django.db import models
from django import forms

from Units.models import Unit
from Users.models import NewUser
from Departments.models import Department
from Rooms.models import Room

# Create your models here.
DAYS_OF_WEEK = (
    ('monday','Monday'),
    ('tuesday','Tuesday'),
    ('wednesday','Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
)

lecturers = NewUser.objects.filter(group='lecturer')


class Lecture(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.SET_DEFAULT, default=None)
    lecturer = models.ForeignKey(NewUser, on_delete=models.SET_DEFAULT, default=None, limit_choices_to={'group':'lecturer'})# Introduce parameter to ensure a lecturer user can only be chosen
    department = models.ForeignKey(Department, on_delete=models.SET_DEFAULT, default=None)
    room = models.ForeignKey(Room, on_delete=models.SET_DEFAULT, default=None)
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    duration = models.IntegerField()
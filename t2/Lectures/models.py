from datetime import datetime

from django.db import models

from Units.models import Unit
from Users.models import NewUser
from Departments.models import Department
from Rooms.models import Room

# Create your models here.
DAYS_OF_WEEK = (
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
)
REASONS = (
    ('lecture','Normal lecture'),
    ('CAT','I want to hold a cat in the room'),
    ('Private class meeting','I want to hold a private meeting in the selected room'),
    ('Group Discussion', 'I want to hold a group study session in the selected room'),
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
    reason = models.CharField(max_length=30, choices=REASONS)
    dateCreated = models.DateTimeField(default=datetime.now())
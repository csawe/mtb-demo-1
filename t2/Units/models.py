from operator import mod
from django.db import models
from Users.models import NewUser

# Create your models here.
class Unit(models.Model):
    unit_code = models.CharField(max_length=8)
    unit_name = models.CharField(max_length=30)
    lecturer = models.ForeignKey(NewUser, on_delete=models.SET_DEFAULT, default=None)
    
    def __str__(self):
        return self.unit_name

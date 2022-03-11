from django.db import models

# Create your models here.
class Time(models.Model):
    time_occupied = models.TimeField()

class Room(models.Model):
    room_id = models.CharField(max_length=5)
    room_location = models.CharField(max_length=20)
    room_carrying_capacity = models.IntegerField()
    functioning_electrical_sockets = models.IntegerField()
    ethernet_ports = models.IntegerField()
    time_occupied = models.ManyToManyField(Time, blank=True, default=None)
    
    def __str__(self):
        return self.room_id

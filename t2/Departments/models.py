from django.db import models

# Create your models here.
class Department(models.Model):
    school = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
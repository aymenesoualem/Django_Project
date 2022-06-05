from pyexpat import model
from django.db import models

# Create your models here.
from django.db import models 

class school(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=100)
    
class course(models.Model):
    name = models.CharField(max_length=30)
    levels = models.IntegerField()
    
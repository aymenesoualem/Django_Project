from django.db import models
class course(models.Model):
    name = models.CharField(max_length=30)
    level = models.IntegerField
    def __str__(self):
       return self.name 
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    courses = course()
    



    def __str__(self):
        return self.first_name + ' ' + self.last_name


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


#Table Teacher
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    patronymic = models.CharField(max_length=240, null=True, blank=True)
    degree = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + " "  + self.last_name + " " + self.patronymic


#Table Student
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    patronymic = models.CharField(max_length=240, null=True, blank=True)
    
    
    def __str__(self):
        return self.first_name + " "  + self.last_name + " " + self.patronymic

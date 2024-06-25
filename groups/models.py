from django.db import models
from acconts.models import Teacher, Student



class Group(models.Model):

    number_group = models.CharField(max_length=100)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.number_group

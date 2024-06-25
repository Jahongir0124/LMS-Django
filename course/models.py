from django.db import models
from acconts.models import Student, Teacher
from groups.models import Group

#Table Course
class Course(models.Model):

    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    item_course = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.name
    
#Table Task
class Task(models.Model):

    name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    answer = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name
    


    


    



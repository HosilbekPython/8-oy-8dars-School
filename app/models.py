from django.contrib.auth.models import User
from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    full_name = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    price = models.IntegerField()
    classs = models.ManyToManyField(Class , related_name="teachers")

    def __str__(self):
        return self.full_name.username



class Student(models.Model):
    full_name = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    classs = models.ForeignKey(Class, on_delete=models.SET_NULL , null=True)

    def __str__(self):
        return self.full_name.username



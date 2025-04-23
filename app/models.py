from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField(max_length=10 , choices=[
        ('admin','Admin'),
        ('teacher','Teacher'),
        ('student','Student')
    ])

class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Admin(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='admin_profile')
    phone_number = models.CharField(max_length=13)
    addres = models.CharField(max_length=255)
    classs = models.ManyToManyField(Class)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='teacher_profile')
    photo = models.ImageField(upload_to="user/teacher/" , null=True , blank=True)
    addres = models.CharField(max_length=255)
    classs = models.ManyToManyField(Class)

    def __str__(self):
        return self.user.username



class Student(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='student_profile')
    photo = models.ImageField(upload_to="user/student/", null=True, blank=True)
    addres = models.CharField(max_length=255)
    classs = models.ForeignKey(Class, on_delete=models.SET_NULL , null=True)

    def __str__(self):
        return self.user.username



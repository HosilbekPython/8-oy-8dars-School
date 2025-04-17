from rest_framework import serializers

from .models import Class , Student , Teacher

class ClassSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class TeacherSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


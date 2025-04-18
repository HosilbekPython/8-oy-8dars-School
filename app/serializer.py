from rest_framework import serializers
from .models import Class , Student , Teacher


class TeacherSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class ClassSerilizer(serializers.ModelSerializer):
    teachers = TeacherSerilizer(many=True , read_only=True)

    class Meta:
        model = Class
        fields = '__all__'

    def create(self, validated_data):
        teachers_data = validated_data.pop("teachers")
        classs = Class.objects.create(**validated_data)
        for teacher_data in teachers_data:
            Teacher.objects.create(classs=classs, **teacher_data)
        return classs

    def update(self, instance, validated_data):
        teachers_data = validated_data.pop("teachers", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if teachers_data is not None:
            instance.teachers.all().delete()
            for teacher_data in teachers_data:
                Teacher.objects.create(classs=instance, **teacher_data)

        return instance




class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


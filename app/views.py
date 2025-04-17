from .models import Class , Teacher , Student
from rest_framework.viewsets import ModelViewSet
from .serializer import ClassSerilizer , TeacherSerilizer , StudentSerilizer

class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerilizer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerilizer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizer



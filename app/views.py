from rest_framework.decorators import permission_classes

from .models import Class , Teacher , Student , Admin
from rest_framework.viewsets import ModelViewSet
from .serializer import ClassSerilizer , TeacherSerilizer , StudentSerilizer , AdminSerializer
from rest_framework import permissions
from .pemrisison import IsAuthenticatedTeacher , IsAuthenticatedUser , IsAdminAndSuperUser

class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerilizer
    permission_classes = [IsAuthenticatedUser, IsAdminAndSuperUser]


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticatedUser, IsAdminAndSuperUser]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerilizer
    permission_classes = [IsAuthenticatedUser, IsAuthenticatedTeacher]


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizer
    permission_classes = [IsAuthenticatedUser]



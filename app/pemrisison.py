from rest_framework.permissions import BasePermission

class IsAdminAndSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.role == 'admin' or request.is_superuser)

class IsAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        return obj.user == request.user


class IsAuthenticatedTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'teacher':
            return True
        return obj.user == request.user






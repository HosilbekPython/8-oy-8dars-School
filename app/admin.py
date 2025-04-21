from django.contrib import admin
from .models import Class , Student , Teacher , User



admin.site.register(User)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)
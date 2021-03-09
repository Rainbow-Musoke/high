from django.contrib import admin
from .models import Student,Teacher,Finance,HOD,Course,Units,Department
# Register your models here.

admin.site.register(Department)
admin.site.register(Units)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Finance)
admin.site.register(HOD)
admin.site.register(Course)


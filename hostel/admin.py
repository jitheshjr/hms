from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['adm_no','name','email','pgm_id']
admin.site.register(Student,StudentAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display=['adm_no','date']
admin.site.register(Attendance,AttendanceAdmin)

admin.site.register(Department)
admin.site.register(Rooms)

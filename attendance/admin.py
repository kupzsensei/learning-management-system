from django.contrib import admin
from .models import Attendance , AttendanceStatus
# Register your models here.
admin.site.register(Attendance)
admin.site.register(AttendanceStatus)
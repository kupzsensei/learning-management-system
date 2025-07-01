from django.db import models
from django.contrib.auth.models import User
from session.models import Session

# Create your models here.
class Attendance(models.Model):
    student = models.ForeignKey(User , on_delete=models.CASCADE)
    session = models.ForeignKey(Session , on_delete=models.CASCADE)
    status = models.ForeignKey('AttendanceStatus' , on_delete=models.CASCADE)

class AttendanceStatus(models.Model):
    name = models.CharField(max_length=20)
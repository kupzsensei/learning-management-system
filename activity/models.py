from django.db import models
from django.contrib.auth.models import User
from session.models import Session

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=100)
    hps = models.IntegerField(default=100)
    description = models.TextField(null=True , blank=True)
    session = models.ForeignKey(Session , on_delete=models.CASCADE)
    file = models.FileField(upload_to='activity/')

class ActivitySubmission(models.Model):
    activity = models.ForeignKey(Activity , on_delete=models.CASCADE)
    student = models.ForeignKey(User , on_delete=models.CASCADE)
    answer = models.TextField()
    file = models.FileField()

class ActivityScore(models.Model):
    activity = models.ForeignKey(Activity , on_delete=models.CASCADE)
    student = models.ForeignKey(User , on_delete=models.CASCADE)
    score = models.IntegerField()
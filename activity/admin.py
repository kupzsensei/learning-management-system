from django.contrib import admin
from .models import Activity , ActivityScore , ActivitySubmission

# Register your models here.

admin.site.register(Activity)
admin.site.register(ActivityScore)
admin.site.register(ActivitySubmission)

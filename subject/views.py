from django.shortcuts import render
from .serializers import SubjectSerializer , SubjectDetailedSerializer
from .models import Subject
from rest_framework import generics
# Create your views here.

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SubjectDetailedSerializer
        return super().get_serializer_class()

from django.shortcuts import render
from rest_framework import generics
from .models import Section
from .serializers import SectionSerializer
# Create your views here.

class SectionView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    

from django.shortcuts import render
from rest_framework import generics
from .models import Section
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .serializers import SectionSerializer, SectionDetailedSerializer


# Create your views here.
class SectionView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    
    def get_serializer_class(self):
        print(self.request.data)
        if self.request.method == "GET":
            return SectionDetailedSerializer
        return super().get_serializer_class()




from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

class GetAllTeacherView(generics.ListAPIView):
    queryset = User.objects.filter(groups__name="Teacher")
    serializer_class = UserSerializer
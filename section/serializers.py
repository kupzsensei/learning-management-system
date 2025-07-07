from rest_framework import serializers
from .models import Section
from core.serializers import UserSerializer
from subject.serializers import SubjectDetailedSerializer , SubjectSerializer

class SectionSerializer(serializers.ModelSerializer):
    # subjects = SubjectSerializer(many=True , write_only=True)
    class Meta:
        model = Section
        fields = ['id' , 'name'  , 'school_year' , 'subjects' , 'students']

class SectionDetailedSerializer(serializers.ModelSerializer):
    students = UserSerializer(many=True , read_only=True)
    subjects = SubjectDetailedSerializer(many=True , read_only=True)
    class Meta:
        model = Section
        fields = '__all__'
        depth = 1
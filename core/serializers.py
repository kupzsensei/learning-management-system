from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['e-mail'] = user.email
        token['lastname'] = user.last_name
        token['roles'] = [group.name for group in user.groups.all()]
        user_permissions = user.get_user_permissions()
        token['persmissions'] = list(user_permissions)

        # ...

        return token
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id" , 'first_name' , "last_name" , "email" , "username"]
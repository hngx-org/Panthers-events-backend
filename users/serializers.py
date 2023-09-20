from rest_framework import serializers
from .models import CustomUserManager, User, Profile



class CustomUserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserManager
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
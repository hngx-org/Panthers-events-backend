from .models import Like
from users.models import User
from rest_framework import serializers

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        # Added For Proper Data Response
        depth = 1

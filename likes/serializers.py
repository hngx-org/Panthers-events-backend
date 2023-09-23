from .models import Likes
# from users.models import Users
from rest_framework import serializers

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'
        # Added For Proper Data Response
        depth = 1

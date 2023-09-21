from rest_framework.serializers import ModelSerializer
from events.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'avatar']

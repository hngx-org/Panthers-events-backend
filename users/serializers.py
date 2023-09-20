from rest_framework.serializers import ModelSerializer
from events.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
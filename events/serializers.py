from rest_framework.serializers import ModelSerializer
from events.models import *


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
        
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
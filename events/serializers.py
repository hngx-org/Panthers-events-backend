from rest_framework.serializers import ModelSerializer
from .models import Event, Comment


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


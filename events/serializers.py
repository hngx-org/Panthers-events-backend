from rest_framework.serializers import ModelSerializer
from events.models import *
from rest_framework import serializers


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
        
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ExpressInterestSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    eventId = serializers.IntegerField()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_Image
        fields = ('image')

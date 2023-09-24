from rest_framework.serializers import ModelSerializer
from events.models import (
    Events, EventThumbnail, InterestedEvents, Images, CommentImages, Comments
    )
from rest_framework import serializers


class EventSerializer(ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class EventThumbnailSerializer(ModelSerializer):
    class Meta:
        model = EventThumbnail
        fields = '__all__'
        
        
class InterestedEventSerializer(ModelSerializer):
    class Meta:
        model = InterestedEvents
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


# class ExpressInterestSerializer(serializers.Serializer):
#     userId = serializers.IntegerField()
#     eventId = serializers.IntegerField()

class RealImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImages
        fields = ['image']

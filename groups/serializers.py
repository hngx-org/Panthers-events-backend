from rest_framework import serializers
from .models import Image, Group, UserGroups, GroupEvents, GroupImage
from users.models import User
from events.models import Event


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserGroupsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())

    class Meta:
        model = UserGroups
        fields = '__all__'


class GroupEventsSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())

    class Meta:
        model = GroupEvents
        fields = '__all__'


class GroupImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupImage
        fields = '__all__'

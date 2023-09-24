from rest_framework import serializers
from .models import Groups, UserGroups, GroupEvents, GroupImage
from users.models import Users
from events.models import Events


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'


class UserGroupsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    group = serializers.PrimaryKeyRelatedField(queryset=Groups.objects.all())

    class Meta:
        model = UserGroups
        fields = '__all__'


class GroupEventsSerializer(serializers.ModelSerializer):
    # event = serializers.PrimaryKeyRelatedField(queryset=Events.objects.all())
    # group = serializers.PrimaryKeyRelatedField(queryset=Groups.objects.all())

    class Meta:
        model = GroupEvents
        fields = '__all__'


class GroupImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupImage
        fields = '__all__'

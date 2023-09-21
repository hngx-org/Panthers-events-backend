from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Group, UserGroups, GroupEvents
from .serializers import GroupSerializer, UserGroupsSerializer, GroupEventsSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserGroupsViewSet(viewsets.ModelViewSet):
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupsSerializer

class GroupEventsViewSet(viewsets.ModelViewSet):
    queryset = GroupEvents.objects.all()
    serializer_class = GroupEventsSerializer
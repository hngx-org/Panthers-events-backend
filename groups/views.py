from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Images, Groups, UserGroups, GroupEvents, GroupImage
from .serializers import (
                          GroupSerializer,
                          UserGroupsSerializer,
                          GroupEventsSerializer,
                          GroupImageSerializer)



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer


class UserGroupsViewSet(viewsets.ModelViewSet):
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupsSerializer


class GroupEventsViewSet(viewsets.ModelViewSet):
    queryset = GroupEvents.objects.all()
    serializer_class = GroupEventsSerializer


class GroupImageViewSet(viewsets.ModelViewSet):
    queryset = GroupImage.objects.all()
    serializer_class = GroupImageSerializer

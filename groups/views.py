from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Images, Groups, UserGroups, GroupEvents, GroupImage
from .serializers import (
                          GroupSerializer,
                          UserGroupsSerializer,
                          GroupEventsSerializer,
                          GroupImageSerializer)
from users.authentication import AuthenticationMiddleware



class GroupViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer


class UserGroupsViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupsSerializer


class GroupEventsViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = GroupEvents.objects.all()
    serializer_class = GroupEventsSerializer


class GroupImageViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = GroupImage.objects.all()
    serializer_class = GroupImageSerializer

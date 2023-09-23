from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Image, Group, UserGroups, GroupEvents, GroupImage
from .serializers import (
    ImageSerializer,
    GroupSerializer,
    UserGroupsSerializer,
    GroupEventsSerializer,
    GroupImageSerializer,
)

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
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

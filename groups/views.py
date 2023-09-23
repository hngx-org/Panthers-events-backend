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

    # def create(self, request, *args, **kwargs):
    #     # Ensure the creator_id is set to the current user when creating a group.
    #     request.data['creator_id'] = request.user.id
    #     serializer = self.get_serializer(data=request.data)
        
    #     if serializer.is_valid():
    #         group = serializer.save()
            
    #         # Add the group creator to the UserGroups relationship
    #         group_owner = request.user
    #         group.usergroups_set.create(user=group_owner)
            
    #         return Response(GroupSerializer(group).data, status=status.HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserGroupsViewSet(viewsets.ModelViewSet):
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupsSerializer

class GroupEventsViewSet(viewsets.ModelViewSet):
    queryset = GroupEvents.objects.all()
    serializer_class = GroupEventsSerializer

class GroupImageViewSet(viewsets.ModelViewSet):
    queryset = GroupImage.objects.all()
    serializer_class = GroupImageSerializer

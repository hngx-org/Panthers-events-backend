from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Group, UserGroups, GroupEvents
from .serializers import GroupSerializer, UserGroupsSerializer, GroupEventsSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class UserGroupsViewSet(viewsets.ModelViewSet):
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupsSerializer

class GroupEventsViewSet(viewsets.ModelViewSet):
    queryset = GroupEvents.objects.all()
    serializer_class = GroupEventsSerializer
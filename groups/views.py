from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Group, UserGroups, GroupEvents
from users.models import User
from .serializers import GroupSerializer, UserGroupsSerializer, GroupEventsSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserGroupsViewSet(viewsets.ModelViewSet):
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupsSerializer

class GroupEventsViewSet(viewsets.ModelViewSet):
    queryset = GroupEvents.objects.all()
    serializer_class = GroupEventsSerializer


class GroupUserView(APIView):
    """ View to handle user actions in a group"""
    permission_classes = [IsAuthenticated]

    def delete(self, request, groupId, userId):
        """Endpoint to remove a user from a group"""
        try:
            group = Group.objects.get(id=groupId)
        except:
            return JsonResponse({"error":"group with id {} does not exist".format(groupId)}, status=status.HTTP_404_NOT_FOUND)
        try:
            user = User.objects.get(id=userId)
        except:
            return JsonResponse({"error":"user with id {} does not exist".format(userId)}, status=status.HTTP_404_NOT_FOUND)

        #get and delete the usergroup object or throw error if user is not in the group
        get_object_or_404(UserGroups, user=user).delete()

        return JsonResponse({"message":"{} has been removed from {} successfully".format(user.username, group.title)}, status=status.HTTP_200_OK)
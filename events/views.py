from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Comment
from groups.models import GroupEvents
from .serializers import CommentSerialzer


class CommentViewSet(viewsets.ModelViewSet):
    serializer = CommentSerialzer

    def queryset(self):
        event_id = self.kwargs['eventId']
        try:
            event = GroupEvents.objects.get(event_id=event_id)
            return Comment.objects.filter(event=event)
        except GroupEvents.DoesNotExist:
            return Comment.objects.none()
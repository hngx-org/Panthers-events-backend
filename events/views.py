from rest_framework.generics import (GenericAPIView, CreateAPIView, 
                                     ListAPIView, RetrieveAPIView)
from django.shortcuts import get_object_or_404
from .models import Event, Comment
from .serializers import EventSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CreateEventAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RetrieveEventAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Verify the event object from the Event model
def get_event_object(eventId):
    if not isinstance(eventId, int):
        return Response({"error": "Event ID must be an integer format."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        event = get_object_or_404(Event, id=eventId)
        return event


class PutDeleteEventDetail(APIView):
    """Update or Delete an event detail."""
    def put(self, request, eventId):
        event = get_event_object(eventId=eventId)

        # Ensure only the event creator can UPDATE the event details
        if request.user == event.creator:
            serializer = EventSerializer(instance=event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You don\'t have permission to make this request.'},
                            status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, eventId):
        event = get_event_object(eventId=eventId)
        # Ensure only the event creator can DELETE the event
        if request.user == event.creator:
            event.delete()
            return Response({'message': 'Event successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'You don\'t have permission to make this request.'},
                            status=status.HTTP_403_FORBIDDEN)


class PostEventComment(APIView):
    """Create a comment for an event."""
    def post(self, request, eventId):
        event = get_event_object(eventId=eventId)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event=event, creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



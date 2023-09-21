from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from events.models import Event, Comment
from events.serializers import EventSerializer, ExpressInterestSerializer, CommentSerializer
from users.models import User
from rest_framework import status, viewsets
from .models import Image, Comment
from .serializers import ImageSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


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


class ExpressInterestView(CreateAPIView):
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        userId = self.kwargs.get('userId')
        eventId = self.kwargs.get('eventId')

        #Validate if user and event exist

        try:
            user = User.objects.get(id=userId)
            event = Event.objects.get(id=eventId)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Event.DoesNotExist:
            return Response({"message": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)

        #creates association between user and event
        user.interested_events.add(event)
        user.save()

        return Response({"message": "Interest expressed successfully"}, status=status.HTTP_201_CREATED)
    
# ADDING IMAGE TO A COMMENT(POST)
class CreateImage(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer = ImageSerializer

    def create(self, request, commentId):
        try:
            comment = Comment.objects.get(id=commentId)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not Found."}, status=status.HTTP_404_NOT_FOUND)
        
        imageData = request.data.get('image')
        if imageData:
            Image.objects.create(comment=comment, image=imageData)
            return Response({"message": "Image added to the comment successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Image data is missing."}, status=status.HTTP_400_BAD_REQUEST)

# GETTING IMAGES FOR A COMMENT(GET)
class ListImage(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer = ImageSerializer

    def list(self, request, commentId):
        try:
            comment = Comment.objects.get(id=commentId)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        
        images = Image.objects.filter(comment=comment)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
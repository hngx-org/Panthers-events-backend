from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from events.serializers import EventSerializer, ExpressInterestSerializer, CommentSerializer
from users.models import Users
from rest_framework import status, viewsets
from .models import CommentImages, Comments, Events, Images, EventThumbnail, InterestedEvents
from .serializers import ImageSerializer, RealImageSerializer, EventThumbnailSerializer, InterestedEventSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from users.authentication import AuthenticationMiddleware,IsAuthenticatedUser


class ImageCreate(ListCreateAPIView):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Images.objects.all()
    serializer_class = RealImageSerializer

class EventListCreateAPIView(ListCreateAPIView):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Events.objects.all()
    serializer_class = EventSerializer


class RetrieveEventAPIView(RetrieveAPIView):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'


class EventThumbnailViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = EventThumbnail.objects.all()
    serializer_class = EventThumbnailSerializer

class InterestedEventsViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = InterestedEvents.objects.all()
    serializer_class = InterestedEventSerializer


# Verify the event object from the Event model
# def get_event_object(eventId):
#     if not isinstance(eventId, int):
#         return Response({"error": "Event ID must be an integer format."}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         event = get_object_or_404(Events, id=eventId)
#         return event


class PutDeleteEventDetail(APIView):
    authentication_classes = [AuthenticationMiddleware]
    permission_classes = [IsAuthenticatedUser]
    """Update or Delete an event detail."""
    def put(self, request, eventId):
        # event = get_event_object(eventId=eventId)
        event = eventId

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
        # event = get_event_object(eventId=eventId)
        event = eventId
        # Ensure only the event creator can DELETE the event
        if request.user == event.creator:
            event.delete()
            return Response({'message': 'Event successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'You don\'t have permission to make this request.'},
                            status=status.HTTP_403_FORBIDDEN)


class PostEventComment(APIView):
    authentication_classes = [AuthenticationMiddleware]
    """Create a comment for an event."""
    def post(self, request, eventId):
        # event = get_event_object(eventId=eventId)
        event = eventId
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event=event, creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpressInterestView(CreateAPIView):
    authentication_classes = [AuthenticationMiddleware]
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        userId = self.kwargs.get('userId')
        eventId = self.kwargs.get('eventId')

        # Validate if user and event exist

        try:
            user = Users.objects.get(id=userId)
            event = Events.objects.get(id=eventId)
        except Users.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Events.DoesNotExist:
            return Response({"message": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # creates association between user and event
        user.interested_events.add(event)
        user.save()

        return Response({"message": "Interest expressed successfully"}, status=status.HTTP_201_CREATED)

class DeleteExpressInterestView(DestroyAPIView):
    authentication_classes = [AuthenticationMiddleware]
    permission_classes = [IsAuthenticatedUser]
    serializer_class = EventSerializer

    def destroy(self, request, *args, **kwargs):
        userId = self.kwargs.get('userId')
        eventId = self.kwargs.get('eventId')

        # Validate if user and event exist

        try:
            user = Users.objects.get(id=userId)
            event = Events.objects.get(id=eventId)
        except Users.DoesNotExist:
            return Response(data={"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Events.DoesNotExist:
            return Response(data={"message": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # deletes association between user and event
        user.interested_events.delete(event)

        return Response(data={"message": "Interest deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# ADDING IMAGE TO A COMMENT(POST)
class CreateImage(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = CommentImages.objects.all()
    serializer = ImageSerializer

    def create(self, request, commentId):
        try:
            comment = Comments.objects.get(id=commentId)
        except Comments.DoesNotExist:
            return Response({"error": "Comment not Found."}, status=status.HTTP_404_NOT_FOUND)

        imageData = request.data.get('image')
        if imageData:
            CommentImages.objects.create(comment=comment, image=imageData)
            return Response({"message": "Image added to the comment successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Image data is missing."}, status=status.HTTP_400_BAD_REQUEST)


# GETTING IMAGES FOR A COMMENT(GET)
class ListImage(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = CommentImages.objects.all()
    serializer = ImageSerializer

    def list(self, request, commentId):
        try:
            comment = Comments.objects.get(id=commentId)
        except Comments.DoesNotExist:
            return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)

        images = CommentImages.objects.filter(comment=comment)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

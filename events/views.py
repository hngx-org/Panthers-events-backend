from rest_framework import viewsets
from .models import Events, EventThumbnail, InterestedEvents, Comments, CommentImages, Images
from .serializers import (
    EventSerializer, EventThumbnailSerializer, InterestedEventSerializer, CommentSerializer,
    RealImageSerializer, ImageSerializer
)
from users.authentication import AuthenticationMiddleware


class EventViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Events.objects.all()
    serializer_class = EventSerializer


class EventThumbnailViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = EventThumbnail.objects.all()
    serializer_class = EventThumbnailSerializer


class InterestedEventViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = InterestedEvents.objects.all()
    serializer_class = InterestedEventSerializer


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class CommentImagesViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = CommentImages.objects.all()
    serializer_class = ImageSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Images.objects.all()
    serializer_class = RealImageSerializer
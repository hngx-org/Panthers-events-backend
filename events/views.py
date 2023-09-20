from rest_framework.generics import (GenericAPIView, CreateAPIView,
                                     ListAPIView, RetrieveAPIView)
from events.models import Event
from django.shortcuts import get_object_or_404
from events.serializers import EventSerializer
from rest_framework.response import Response
from users.models import User
import status as status


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CreateEventAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RetrieveEventAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ExpressInterestView(GenericAPIView):
    serializer_class = EventSerializer

    @staticmethod
    def post(request, userId, eventId):
        try:
            user = get_object_or_404(User, id=userId)
            event = get_object_or_404(Event, id=eventId)

            user.interested_events.add(event)

            return Response({"message": f"User {userId} has expressed interest in Event {eventId}"},
                            status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"error": f"User {userId} does not exist"},
                            status=status.HTTP_404_NOT_FOUND)
        except Event.DoesNotExist:
            return Response({"error":f"Event {eventId} does not exist"},
                            status=status.HTTP_404_NOT_FOUND)



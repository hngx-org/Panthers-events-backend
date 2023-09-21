from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from events.models import Event
from events.serializers import EventSerializer, ExpressInterestSerializer
from users.models import User
from rest_framework import status
from rest_framework.response import Response


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CreateEventAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RetrieveEventAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ExpressInterestView(CreateAPIView):
    serializer_class = ExpressInterestSerializer

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

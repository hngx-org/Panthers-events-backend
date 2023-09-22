from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class SingleUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    lookup_field = 'id'  # Set the lookup field to 'id'
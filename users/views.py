from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Users

# Create your views here.
class UserView(generics.ListCreateAPIView):
    queryset = Users.objects,all()
    serializer = UserSerializer

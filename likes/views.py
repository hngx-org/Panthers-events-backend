from django.shortcuts import render
from .serializers import LikeSerializer
from .models import Like
from rest_framework import generics

# Create your views here.
class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDetail(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
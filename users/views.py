from django.shortcuts import render,redirect
from rest_framework import generics
from rest_framework.response import Response
from django.views import View
from .serializers import UserSerializer
from .models import User
from authlib.integrations.django_client import OAuth
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse
import uuid

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile',
    }
)

# Create your views here.
class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class SingleUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'  # Set the lookup field to 'id'
    
    
class LoginView(View):
    def get(self, request):
        redirect_uri = request.build_absolute_uri(reverse('auth'))
        return oauth.google.authorize_redirect(request, redirect_uri)

class AuthView(View):
    def get(self, request):
        token = oauth.google.authorize_access_token(request)
        
        User = get_user_model() 
        email = token.get('userinfo', {}).get('email')
        name = token.get('userinfo', {}).get('name')
        picture = token.get('userinfo', {}).get('picture')
        id = token.get('userinfo', {}).get('sub')
        # access_token = token.get('access_token', {})
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User.objects.create(email=email, id=str(id), name=name, avatar=picture)
                    
        user_serializer = UserSerializer(user)
        
        redirect_uri = request.build_absolute_uri(reverse('user_detail', kwargs={"id": user.id}))
        
        return redirect(redirect_uri)

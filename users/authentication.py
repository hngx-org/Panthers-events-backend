from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from itsdangerous import URLSafeTimedSerializer
from .models import Users
from rest_framework import permissions

class AuthenticationMiddleware(authentication.BaseAuthentication):
    secret_key = settings.SECRET_KEY 

    def authenticate(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION', '')
        token = authorization_header.split(' ')[1] if authorization_header.startswith('Bearer ') else ''

        if not token:
            raise exceptions.AuthenticationFailed()

        serializer = URLSafeTimedSerializer(self.secret_key)
        try:
            user_id = serializer.loads(token, max_age=2592000)  # Adjust expiration time if needed
        except:
            raise exceptions.AuthenticationFailed()

        if user_id:
            try:
                user = Users.objects.get(id=user_id)
                request.user = user
                return (user, None)  # Return a tuple with user object and None for successful authentication
            except Users.DoesNotExist:
                pass

        raise exceptions.AuthenticationFailed('Invalid or expired token')  # Raise AuthenticationFailed for failed authentication
    
    
    
class IsAuthenticatedUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
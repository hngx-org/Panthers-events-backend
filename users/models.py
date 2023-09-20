from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class Users(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length= 60, primary_key=True, blank=None)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=120)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
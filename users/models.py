from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200 ,blank=True)
    email = models.EmailField(unique=True)
    avatar = models.URLField(max_length=250,blank=True)
    
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['name', 'email', 'avatar']
    
    def __str__(self):
        return self.name
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True
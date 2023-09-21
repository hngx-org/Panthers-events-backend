from django.db import models


class User(models.Model):
    id = models.CharField(max_length=60, primary_key=True, editable=False)
    name = models.CharField(max_length=255 ,blank=True)
    email = models.CharField(max_length=255, unique=True)
    avatar = models.CharField(max_length=255,blank=True)
    
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
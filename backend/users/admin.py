from django.contrib import admin
from .models import CustomUserManager, User, Profile

# Register your models here.
# admin.site.register(CustomUserManager)
admin.site.register(User)
admin.site.register(Profile)
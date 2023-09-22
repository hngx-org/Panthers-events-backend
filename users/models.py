from django.db import models

class User(models.Model):
    id = models.CharField(max_length= 60, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    avatar = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['name', 'email', 'avatar', 'created_at', 'updated_at']
    
    def __str__(self):
        return self.name
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True


# from django.db import models
# from django.contrib.auth.models import  ( AbstractBaseUser, BaseUserManager, PermissionsMixin )

# from helpers.models import CustomModel

# # Create your models here.
# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **kwargs):
#         if username is None:
#             raise TypeError('Users should have a username')
#         if email is None:
#             raise TypeError('Users should have a Email')

#         email = self.normalize_email(email)
#         user = self.model(username=username, email = email, **kwargs)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, username, email, password=None, **kwargs):
#         if password is None:
#             raise TypeError('Password should not be none')

#         user = self.create_user(username, email, password, **kwargs)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user



# class User(AbstractBaseUser, PermissionsMixin, CustomModel):
#     username = models.CharField(max_length=255, unique=True, db_index=True)
#     email = models.EmailField(max_length=255, unique=True, db_index=True)
#     referral_code = models.CharField(max_length=255, blank=True)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     objects = UserManager()

#     def __str__(self):
#         return self.email


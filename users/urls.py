from django.urls import path
from . import views

urlpatterns = [
    path('api/user', views.UserView.as_view()),
    
]
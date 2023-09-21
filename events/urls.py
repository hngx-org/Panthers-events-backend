from django.urls import path
from . import views



urlpatterns = [
    path('api/events/', views.EventListAPIView.as_view(), name='event-list'),
    path('api/events/', views.CreateEventAPIView.as_view(), name='event-create'),
    path('api/events/<int:pk>/', views.RetrieveEventAPIView.as_view(), name='event-retrieve'),
]


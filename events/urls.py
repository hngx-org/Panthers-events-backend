from django.urls import path
from . import views



urlpatterns = [
    path('api/events/', views.EventListAPIView.as_view(), name='event-list'),
    path('api/events/', views.EventCreateAPIView.as_view(), name='event-create'),
    path('api/events/<int:pk>/', views.EventRetrieveAPIView.as_view(), name='event-retrieve'),
]


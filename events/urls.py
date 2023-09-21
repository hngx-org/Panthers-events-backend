from django.urls import path
from . import views


urlpatterns = [
    path('api/events/', views.EventListAPIView.as_view(), name='event-list'),
    path('api/events/', views.CreateEventAPIView.as_view(), name='event-create'),
    path('api/events/<int:pk>/', views.EventRetrieveAPIView.as_view(), name='event-retrieve'),
    path('api/users/<int:userId>/interests/<int:eventId>/', views.ExpressInterestView.as_view(),
         name='express-interest'),
    path('api/users/<int:userId>/interests/<int:eventId>/',views.DeleteExpressInterestView.as_view(),name='delete-express-interest'),     
]

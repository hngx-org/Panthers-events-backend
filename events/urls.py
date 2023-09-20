from django.urls import path
import views


urlpatterns = [
    path('events/', views.CreateAPIView.as_view(), name='create-event'),
    path('events/<int:id>/', views.RetrieveAPIView.as_view(), name='event-detail'),
    path('events/', views.EventListAPIView.as_view(), name='event-list'),

    path('<int:eventId>/', views.PutDeleteEventDetail.as_view(), name='event_detail'),
    path('<int:eventId>/comments/', views.PostEventComment.as_view(), name='event_comment'),
]

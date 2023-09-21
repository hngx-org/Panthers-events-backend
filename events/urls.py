from django.urls import path
from . import views
from . views import CreateImage, ListImage


urlpatterns = [
    path('api/events/', views.EventListCreateAPIView.as_view(), name='event-list'),
    # path('api/events/', views.CreateEventAPIView.as_view(), name='event-create'),
    path('api/events/<int:pk>/', views.RetrieveEventAPIView.as_view(), name='event-retrieve'),

    path('api/events/<int:eventId>/', views.PutDeleteEventDetail.as_view(), name='event_detail'),
    path('api/events/<int:eventId>/comments/', views.PostEventComment.as_view(), name='event_comment'),

    path('api/users/<int:userId>/interests/<int:eventId>/', views.ExpressInterestView.as_view(),
         name='express-interest'),
    path('api/users/<int:userId>/interests/<int:eventId>/',views.DeleteExpressInterestView.as_view(),name='delete-express-interest'),     

    path('api/comments/<int:commentId>/images/', CreateImage.as_view({'post': 'create'}), name='add-comment-image'),
    path('api/comments/<int:commentId>/images/list/', ListImage.as_view({'get': 'list'}), name='list-comment-images'),
]

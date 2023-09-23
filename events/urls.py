from django.urls import path
from . import views
from . views import CreateImage, ListImage, ImageCreate
from groups.urls import router


urlpatterns = [
    path('events/', views.EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<str:pk>/', views.RetrieveEventAPIView.as_view(), name='event-retrieve'),
    path('events/<str:eventId>/comments', views.PostEventComment.as_view(), name='event_comment'),
    path('events/del/<str:eventId>/', views.PutDeleteEventDetail.as_view(), name='event_comment'),

    path('images/', ImageCreate.as_view(), name='images'),

    path('users/<str:userId>/interests/<str:eventId>/', views.ExpressInterestView.as_view(),
         name='express-interest'),
    path('users/<str:userId>/interests/<str:eventId>/',views.DeleteExpressInterestView.as_view(),name='delete-express-interest'),     

    path('comments/<str:commentId>/images/', CreateImage.as_view({'post': 'create'}), name='add-comment-image'),
    path('comments/<str:commentId>/images/list/', ListImage.as_view({'get': 'list'}), name='list-comment-images')
] + router.urls

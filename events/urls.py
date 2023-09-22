from django.urls import path
from . import views
from . views import CreateImage, ListImage


urlpatterns = [
    path('events/', views.EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', views.RetrieveEventAPIView.as_view(), name='event-retrieve'),

    path('users/<int:userId>/interests/<int:eventId>/', views.ExpressInterestView.as_view(),
         name='express-interest'),
    path('users/<int:userId>/interests/<int:eventId>/',views.DeleteExpressInterestView.as_view(),name='delete-express-interest'),     

    path('comments/<int:commentId>/images/', CreateImage.as_view({'post': 'create'}), name='add-comment-image'),
    path('comments/<int:commentId>/images/list/', ListImage.as_view({'get': 'list'}), name='list-comment-images')
]

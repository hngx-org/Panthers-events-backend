from django.urls import path
from . import views
from . views import CreateImage, ListImage


urlpatterns = [
    path('api/events/', views.EventListCreateAPIView.as_view(), name='event-list-create'),
    path('api/events/<int:pk>/', views.RetrieveEventAPIView.as_view(), name='event-retrieve'),

    path('api/users/<int:userId>/interests/<int:eventId>/', views.ExpressInterestView.as_view(),
         name='express-interest'),
    path('api/users/<int:userId>/interests/<int:eventId>/',views.DeleteExpressInterestView.as_view(),name='delete-express-interest'),     

    path('api/comments/<int:commentId>/images/', CreateImage.as_view({'post': 'create'}), name='add-comment-image'),
    path('api/comments/<int:commentId>/images/list/', ListImage.as_view({'get': 'list'}), name='list-comment-images')
]

from django.urls import path
from . import views

urlpatterns = [
    path('likes/', views.LikeList.as_view(), name='likes'),
    path('likes/<int:pk>', views.LikeDetail.as_view(), name='likes-detail'),
]
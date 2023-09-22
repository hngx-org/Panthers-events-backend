from django.urls import path
from . import views


urlpatterns = [
    path('api/user/<str:id>', views.SingleUserView.as_view(),name="user_detail"),
]
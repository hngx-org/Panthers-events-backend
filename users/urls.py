from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.UserView.as_view(), name="user_list"),
    path('user/<str:id>', views.SingleUserView.as_view(),name="user_detail"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('auth/', views.AuthView.as_view(), name='auth'),
]
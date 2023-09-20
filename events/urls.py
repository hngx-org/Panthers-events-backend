from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'event', EventViewSet)
router.register(r"comment",CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

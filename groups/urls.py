from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ImageViewSet,
                    GroupViewSet,
                    UserGroupsViewSet,
                    GroupEventsViewSet,
                    GroupImageViewSet)


router = DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'usergroups', UserGroupsViewSet)
router.register(r'groupevents', GroupEventsViewSet)
router.register(r'group-images', GroupImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
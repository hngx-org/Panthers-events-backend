from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
                    GroupViewSet,
                    UserGroupsViewSet,
                    GroupEventsViewSet,
                    GroupImageViewSet,
                    ImageViewSet,
                    )
router = DefaultRouter()
router.register(r'groups', GroupViewSet, basename='groups')
# router.register(r'groups/<str:id>', GroupViewSet)
router.register(r'usergroups', UserGroupsViewSet)
router.register(r'groupevents', GroupEventsViewSet)
router.register(r'groupimages', GroupImageViewSet)
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

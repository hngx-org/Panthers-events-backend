from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, UserGroupsViewSet, GroupEventsViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'usergroups', UserGroupsViewSet)
router.register(r'groupevents', GroupEventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

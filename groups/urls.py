from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, UserGroupsViewSet, GroupEventsViewSet
from events.views import CommentViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'usergroups', UserGroupsViewSet)
router.register(r'groupevents', GroupEventsViewSet)
router.register(r'groupevents/(?P<event_id>[^/.]+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]

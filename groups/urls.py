from django.urls import path, include
from rest_framework.routers import DefaultRouter
from likes.views import LikeViewSet
from events.views import (
    EventViewSet, EventThumbnailViewSet, InterestedEventViewSet,
    CommentViewSet, CommentImagesViewSet, ImagesViewSet
)
from .views import (
                    GroupViewSet,
                    UserGroupsViewSet,
                    GroupEventsViewSet,
                    GroupImageViewSet,
                    )

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'event-thumbnails', EventThumbnailViewSet)
router.register(r'interested-events', InterestedEventViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'comment-images', CommentImagesViewSet)
router.register(r'images', ImagesViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'usergroups', UserGroupsViewSet)
router.register(r'groupevents', GroupEventsViewSet)
router.register(r'groupimages', GroupImageViewSet)
router.register(r'likes', LikeViewSet)
# from .views import (
#                     GroupViewSet,
#                     UserGroupsViewSet,
#                     GroupEventsViewSet,
#                     GroupImageViewSet,
#                     )
# router = DefaultRouter()
# router.register(r'groups', GroupViewSet, basename='groups')
# # router.register(r'groups/<str:id>', GroupViewSet)
# router.register(r'usergroups', UserGroupsViewSet)
# router.register(r'groupevents', GroupEventsViewSet)
# router.register(r'groupimages', GroupImageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

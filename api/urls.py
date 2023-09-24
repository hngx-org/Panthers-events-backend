from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from likes.views import LikeViewSet
from events.views import (
    EventViewSet, EventThumbnailViewSet, InterestedEventViewSet,
    CommentViewSet, CommentImagesViewSet, ImagesViewSet
)
from groups.views import (
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

schema_view = get_schema_view(
    openapi.Info(
        title="Team Panther EventAPI",
        default_version="v1",
        description="This is the Team Panther event application to manage events for our users.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
     path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    # path("api/", include("groups.urls") ),
    # path("api/", include("events.urls") ),
    path("api/", include("users.urls") ),
    # Added Endpoint for Listing a comment Like
    # path("api/", include("likes.urls") ),
    path('api/', include(router.urls)),
]

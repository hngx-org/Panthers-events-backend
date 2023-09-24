from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    path("api/", include("groups.urls") ),
    # path("api/", include("events.urls") ),
    path("api/", include("users.urls") ),
    # Added Endpoint for Listing a comment Like
    # path("api/", include("likes.urls") ),
]

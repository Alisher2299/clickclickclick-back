from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

Router = DefaultRouter if settings.DEBUG else SimpleRouter
router = Router(trailing_slash=settings.APPEND_SLASH)

urlpatterns = [
    path("v1/clicks/", include("clicks.urls")),
]

urlpatterns += router.urls

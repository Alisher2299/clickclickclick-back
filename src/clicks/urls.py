from django.conf import settings

from rest_framework.routers import DefaultRouter, SimpleRouter

from clicks.views import UserClickViewSet, CountryStatisticViewSet

Router = DefaultRouter if settings.DEBUG else SimpleRouter
router = Router(trailing_slash=settings.APPEND_SLASH)

router.register("user-click", UserClickViewSet, basename="user_click")
router.register("statistic", CountryStatisticViewSet, basename="statistic")

urlpatterns = [
]

urlpatterns += router.urls

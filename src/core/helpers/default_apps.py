from typing import Tuple

DJANGO_APPS: Tuple[str, ...] = (
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.messages",
    "django.contrib.sessions",
)
SIDE_APPS: Tuple[str, ...] = (
    "corsheaders",
    "rest_framework",
    "django_extensions",
)
PROJECT_APPS: Tuple[str, ...] = (
    "clicks.apps.ClicksConfig",
)
message: str = "no more than 9 apps per django project"
assert len(PROJECT_APPS) <= 9, message  # nosec
DEFAULT_APPS: Tuple[str, ...] = DJANGO_APPS + SIDE_APPS + PROJECT_APPS

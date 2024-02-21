from os.path import join
from pathlib import Path
from types import MappingProxyType
from typing import Tuple, List, Dict, Callable, Any

from corsheaders.defaults import default_methods, default_headers

from environ import Env

from core.helpers import (
    DEFAULT_APPS, DEFAULT_MIDDLEWARE, DEFAULT_LOCALE_PATHS, DEFAULT_LANGUAGES,
    DEFAULT_AUTH_PASSWORD_VALIDATORS, DEFAULT_TEMPLATES,
)
from telegram import Bot
from telegram.ext import Updater

BASE_DIR = Path(__file__).resolve().parent.parent
# Environment variables
env: Env = Env()
Env.read_env()

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django
INSTALLED_APPS: Tuple = DEFAULT_APPS
MIDDLEWARE: Tuple = DEFAULT_MIDDLEWARE
SECRET_KEY: str = env.str(var="SECRET_KEY")
DEBUG: bool = env.bool(var="DEBUG")
LOCAL: bool = env.bool(var="LOCAL", default=True)
ALLOWED_HOSTS: Tuple = (
    "*",
    "164.92.179.32"
)
ADMIN_URL = env.str(var="DJANGO_ADMIN_URL")
HOST = env.str(var="HOST", default='')
ROOT_URLCONF: str = "core.urls"
WSGI_APPLICATION = 'core.wsgi.application'
APPEND_SLASH: bool = True
DATABASES: MappingProxyType = MappingProxyType({"default": env.db()})
# AUTHENTICATION
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
# ---------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "django.contrib.auth.backends.RemoteUserBackend",
]
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# PASSWORD_HASHERS: Tuple = DEFAULT_PASSWORD_HASHERS
AUTH_PASSWORD_VALIDATORS: Tuple = DEFAULT_AUTH_PASSWORD_VALIDATORS
# ASGI
ASGI_APPLICATION: str = "core.asgi.application"
# Security
SECURE_BROWSER_XSS_FILTER: bool = True
X_FRAME_OPTIONS: str = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF: bool = True
# CorsHeaders
CORS_ORIGIN_ALLOW_ALL: bool = True
CORS_ALLOW_METHODS: Tuple = default_methods
CORS_ALLOW_HEADERS: Tuple = default_headers
CORS_ALLOW_CREDENTIALS: bool = True

# Localization
LOCALE_PATHS: List = DEFAULT_LOCALE_PATHS
LANGUAGES: Tuple = DEFAULT_LANGUAGES
LANGUAGE_CODE: str = "ru"
USE_I18N: bool = True
TIME_ZONE: str = env.str(var="TIME_ZONE")
USE_TZ: bool = True

# STATIC
# ------------------------
STATIC_URL: str = "/static/"
STATIC_ROOT: str = join(BASE_DIR, "staticfiles")
# MEDIA
MEDIA_URL: str = "/media/"
MEDIA_ROOT: str = join(BASE_DIR, "media")
TEMPLATES: Tuple = DEFAULT_TEMPLATES

# Silk
SILKY_PYTHON_PROFILER: bool = True
SILKY_META: bool = True
SILKY_INTERCEPT_PERCENT: int = env.int(var="SILKY_INTERCEPT_PERCENT")
SILKY_MAX_RECORDED_REQUESTS: int = 8192
SILKY_AUTHENTICATION: bool = True
SILKY_AUTHORISATION: bool = True
SILKY_PERMISSIONS: Callable[[Any], Any] = lambda user: user.is_superuser

# Celery
CELERY_BROKER_URL: str = env.str(var="CELERY_BROKER_URL")
CELERY_RESULT_BACKEND: str = 'rpc'
CELERY_TIMEZONE: str = "Asia/Almaty"
CELERY_RESULT_EXPIRES: int = 60
CELERY_TASK_RESULT_EXPIRES: int = 60
CELERY_IGNORE_RESULT: bool = True
CELERY_TASK_IGNORE_RESULT = True

# Telegram
TELEGRAM_API_TOKEN: str = env.str(var="TELEGRAM_API_TOKEN")
TELEGRAM_BOT: Bot = Updater(TELEGRAM_API_TOKEN).bot
TELEGRAM_CHAT_ID: int = env.int(var="TELEGRAM_CHAT_ID")

# SECURITY SETTINGS
SECURE_HSTS_SECONDS = 120
SECURE_SSL_REDIRECT: bool = env.bool(var="DJANGO_SECURE_SSL_REDIRECT")
SESSION_COOKIE_SECURE: bool = env.bool(var="DJANGO_SESSION_COOKIE_SECURE")
CSRF_COOKIE_SECURE: bool = env.bool(var="DJANGO_CSRF_COOKIE_SECURE")
SECURE_HSTS_INCLUDE_SUBDOMAINS: bool = env.bool(var="DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS")
SECURE_HSTS_PRELOAD: bool = env.bool(var="DJANGO_SECURE_HSTS_PRELOAD")
FREEDOM_MOBILE_SMS_VERIFY_URL = ''
# Debug toolbar
if DEBUG:
    from .helpers.debug_settings import (
        DEFAULT_DEBUG_MIDDLEWARE,
        DEFAULT_DEBUG_INTERNAL_IPS,
        DEFAULT_DEBUG_TOOLBAR_PANELS,
        DEFAULT_DEBUG_APPS,
        DEFAULT_DEBUG_TOOLBAR_CONFIG,
    )

    # Debug
    INSTALLED_APPS += DEFAULT_DEBUG_APPS
    MIDDLEWARE += DEFAULT_DEBUG_MIDDLEWARE
    INTERNAL_IPS: Tuple = DEFAULT_DEBUG_INTERNAL_IPS
    DEBUG_TOOLBAR_PANELS: Tuple = DEFAULT_DEBUG_TOOLBAR_PANELS
    DEBUG_TOOLBAR_CONFIG: Dict = DEFAULT_DEBUG_TOOLBAR_CONFIG

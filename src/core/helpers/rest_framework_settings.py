import datetime
from types import MappingProxyType

VERSIONING = "rest_framework.versioning.AcceptHeaderVersioning"
PAGINATION = "rest_framework.pagination.PageNumberPagination"

REST_FRAMEWORK_SETTINGS = MappingProxyType(
    mapping={
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ),
        "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
        "DEFAULT_VERSIONING_CLASS": VERSIONING,
        "DEFAULT_VERSION": "1.0",
        "ALLOWED_VERSIONS": ("1.0",),
        "DEFAULT_PAGINATION_CLASS": PAGINATION,
        "PAGE_SIZE": 15,
    },
)

# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT_SETTINGS = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
}

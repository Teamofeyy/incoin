import os

from .base import *  # noqa

DEBUG = False


def split_env(name, default=""):
    return [
        item.strip()
        for item in os.getenv(name, default).split(",")
        if item.strip()
    ]


DOMAIN = os.getenv("DOMAIN", "localhost")

ALLOWED_HOSTS += [DOMAIN, *split_env("PRODUCTION_HOSTS", "backend")]

CORS_ALLOW_ALL_ORIGINS = (
    os.getenv("CORS_ALLOW_ALL_ORIGINS", "False").lower() == "true"
)
CORS_ALLOWED_ORIGINS = split_env(
    "CORS_ALLOWED_ORIGINS",
    f"https://{DOMAIN},http://{DOMAIN}",
)

CSRF_TRUSTED_ORIGINS = split_env(
    "CSRF_TRUSTED_ORIGINS",
    f"https://{DOMAIN},http://{DOMAIN}",
)

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "True").lower() == "true"

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

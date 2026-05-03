from django.conf import settings
from django.http import HttpRequest


def site(request: HttpRequest) -> dict[str, str | dict[str, str]]:
    return {
        "site_name": settings.SITE_NAME,
        "theme": settings.THEME,
    }

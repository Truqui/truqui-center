from django.conf import settings
from django.db.models import QuerySet
from django.http import HttpRequest

from src.infrastructure.database.menu.models import MenuItem
from src.infrastructure.database.menu.queries import get_active_menu_items


def site(request: HttpRequest) -> dict[str, str | dict[str, str] | QuerySet[MenuItem]]:
    return {
        "site_name": settings.SITE_NAME,
        "theme": settings.THEME,
        "menu_items": get_active_menu_items(),
    }

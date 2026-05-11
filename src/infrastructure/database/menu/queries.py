from django.db.models import QuerySet

from src.infrastructure.database.menu.models import MenuItem


def get_active_menu_items() -> QuerySet[MenuItem]:
    return MenuItem.objects.filter(is_active=True).order_by("order", "id")

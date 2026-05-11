from django.contrib import admin

from src.infrastructure.database.menu.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ["label", "url", "order", "is_active"]
    list_editable = ["order", "is_active"]

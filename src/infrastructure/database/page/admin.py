from django.contrib import admin

from src.infrastructure.database.page.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ["title", "slug", "is_published", "published_at"]
    prepopulated_fields = {"slug": ("title",)}

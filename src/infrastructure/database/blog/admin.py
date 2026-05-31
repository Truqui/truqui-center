from django.contrib import admin

from src.infrastructure.database.blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ["title", "slug", "is_published", "published_at"]
    prepopulated_fields = {"slug": ("title",)}

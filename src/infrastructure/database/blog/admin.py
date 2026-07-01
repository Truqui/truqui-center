from django.contrib import admin
from django.db.models import F, QuerySet
from django.http import HttpRequest

from src.infrastructure.database.blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ["title", "slug", "is_published", "published_at"]
    prepopulated_fields = {"slug": ("title",)}

    def get_queryset(self, request: HttpRequest) -> QuerySet[Post]:
        return Post.objects.order_by(F("published_at").desc(nulls_last=True), "-pk")

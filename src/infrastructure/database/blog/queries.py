from django.db.models import F, QuerySet

from src.infrastructure.database.blog.models import Post


def get_published_posts() -> QuerySet[Post]:
    return Post.objects.filter(is_published=True).order_by(
        F("published_at").desc(nulls_last=True), "-pk"
    )

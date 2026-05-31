from django.db.models import QuerySet
from django.views.generic import DetailView

from src.infrastructure.database.blog.models import Post


class PostDetailView(DetailView):  # type: ignore[type-arg]
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self) -> QuerySet[Post]:
        return Post.objects.filter(is_published=True)

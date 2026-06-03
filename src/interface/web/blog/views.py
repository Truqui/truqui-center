from django.db.models import QuerySet
from django.views.generic import DetailView, ListView

from src.infrastructure.database.blog.models import Post


class PostListView(ListView):  # type: ignore[type-arg]
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Post]:
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):  # type: ignore[type-arg]
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self) -> QuerySet[Post]:
        return Post.objects.filter(is_published=True)

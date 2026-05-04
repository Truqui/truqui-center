from django.db.models import QuerySet
from django.views.generic import DetailView

from src.infrastructure.database.page.models import Page


class PageDetailView(DetailView):  # type: ignore[type-arg]
    template_name = "page/page_detail.html"
    context_object_name = "page"

    def get_queryset(self) -> QuerySet[Page]:
        return Page.objects.filter(is_published=True)

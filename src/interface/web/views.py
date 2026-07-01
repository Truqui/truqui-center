from django.http import HttpRequest, HttpResponseBase
from django.shortcuts import render
from django.views import View

from src.infrastructure.database.settings.models import SiteSettings
from src.interface.web.blog.views import PostListView


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponseBase:
        site_settings = SiteSettings.get()

        if (
            site_settings.home_mode == SiteSettings.HomeMode.PAGE
            and site_settings.home_page_id is not None
            and site_settings.home_page.is_published  # type: ignore[union-attr]
        ):
            return render(
                request, "page/page_detail.html", {"page": site_settings.home_page}
            )

        return PostListView.as_view()(request)

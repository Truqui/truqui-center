from django.test import TestCase

from src.infrastructure.database.page.models import Page


class PageDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.published_page = Page.objects.create(
            title="About",
            slug="about",
            content="About me",
            is_published=True,
        )
        self.draft_page = Page.objects.create(
            title="Draft",
            slug="draft",
            content="Not ready",
            is_published=False,
        )

    def test_published_page_returns_200(self) -> None:
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_unpublished_page_returns_404(self) -> None:
        response = self.client.get("/draft/")
        self.assertEqual(response.status_code, 404)

    def test_unknown_slug_returns_404(self) -> None:
        response = self.client.get("/does-not-exist/")
        self.assertEqual(response.status_code, 404)

    def test_context_contains_page(self) -> None:
        response = self.client.get("/about/")
        self.assertIn("page", response.context)
        self.assertEqual(response.context["page"], self.published_page)

    def test_uses_page_detail_template(self) -> None:
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "page/page_detail.html")

from django.test import TestCase

from src.infrastructure.database.blog.models import Post


class PostDetailViewTest(TestCase):
    def setUp(self) -> None:
        self.published_post = Post.objects.create(
            title="Hello World",
            slug="hello-world",
            content="My first post",
            is_published=True,
        )
        self.draft_post = Post.objects.create(
            title="Draft",
            slug="draft",
            content="Not ready",
            is_published=False,
        )

    def test_published_post_returns_200(self) -> None:
        response = self.client.get("/blog/hello-world/")
        self.assertEqual(response.status_code, 200)

    def test_unpublished_post_returns_404(self) -> None:
        response = self.client.get("/blog/draft/")
        self.assertEqual(response.status_code, 404)

    def test_unknown_slug_returns_404(self) -> None:
        response = self.client.get("/blog/does-not-exist/")
        self.assertEqual(response.status_code, 404)

    def test_context_contains_post(self) -> None:
        response = self.client.get("/blog/hello-world/")
        self.assertIn("post", response.context)
        self.assertEqual(response.context["post"], self.published_post)

    def test_uses_post_detail_template(self) -> None:
        response = self.client.get("/blog/hello-world/")
        self.assertTemplateUsed(response, "blog/post_detail.html")

from django.test import TestCase

from src.infrastructure.database.blog.models import Post


class PostListViewTest(TestCase):
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

    def test_returns_200(self) -> None:
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_only_published_posts_appear(self) -> None:
        response = self.client.get("/blog/")
        posts = list(response.context["posts"])
        self.assertIn(self.published_post, posts)
        self.assertNotIn(self.draft_post, posts)

    def test_uses_post_list_template(self) -> None:
        response = self.client.get("/blog/")
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_pagination(self) -> None:
        for i in range(10):
            Post.objects.create(
                title=f"Post {i}",
                slug=f"post-{i}",
                content="content",
                is_published=True,
            )
        response = self.client.get("/blog/")
        self.assertTrue(response.context["is_paginated"])
        response_p2 = self.client.get("/blog/?page=2")
        self.assertEqual(response_p2.status_code, 200)


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

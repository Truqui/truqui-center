from django.test import TestCase

from src.infrastructure.database.blog.models import Post
from src.infrastructure.database.page.models import Page
from src.infrastructure.database.settings.models import SiteSettings


class HomeViewBlogModeTest(TestCase):
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
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_uses_post_list_template(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_only_published_posts_appear(self) -> None:
        response = self.client.get("/")
        posts = list(response.context["posts"])
        self.assertIn(self.published_post, posts)
        self.assertNotIn(self.draft_post, posts)

    def test_site_name_in_context(self) -> None:
        response = self.client.get("/")
        self.assertIn("site_name", response.context)


class HomeViewPageModeTest(TestCase):
    def setUp(self) -> None:
        self.page = Page.objects.create(
            title="About",
            slug="about",
            content="content",
            is_published=True,
        )
        settings = SiteSettings.get()
        settings.home_mode = SiteSettings.HomeMode.PAGE
        settings.home_page = self.page
        settings.save()

    def test_returns_200(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_uses_page_detail_template(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "page/page_detail.html")

    def test_context_contains_home_page(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.context["page"], self.page)


class HomeViewPageModeWithoutHomePageTest(TestCase):
    def setUp(self) -> None:
        self.published_post = Post.objects.create(
            title="Hello World",
            slug="hello-world",
            content="My first post",
            is_published=True,
        )
        settings = SiteSettings.get()
        settings.home_mode = SiteSettings.HomeMode.PAGE
        settings.save()

    def test_falls_back_to_blog_list(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "blog/post_list.html")
        self.assertIn(self.published_post, list(response.context["posts"]))


class HomeViewPageModeWithUnpublishedHomePageTest(TestCase):
    def setUp(self) -> None:
        self.published_post = Post.objects.create(
            title="Hello World",
            slug="hello-world",
            content="My first post",
            is_published=True,
        )
        self.page = Page.objects.create(
            title="Draft page",
            slug="draft-page",
            content="content",
            is_published=False,
        )
        settings = SiteSettings.get()
        settings.home_mode = SiteSettings.HomeMode.PAGE
        settings.home_page = self.page
        settings.save()

    def test_falls_back_to_blog_list(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "blog/post_list.html")
        self.assertIn(self.published_post, list(response.context["posts"]))

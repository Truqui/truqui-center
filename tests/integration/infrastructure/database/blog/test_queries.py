from django.test import TestCase
from django.utils import timezone

from src.infrastructure.database.blog.models import Post
from src.infrastructure.database.blog.queries import get_published_posts


class GetPublishedPostsTest(TestCase):
    def test_only_published_posts_are_returned(self) -> None:
        published = Post.objects.create(
            title="Published",
            slug="published",
            content="content",
            is_published=True,
            published_at=timezone.now(),
        )
        Post.objects.create(
            title="Draft",
            slug="draft",
            content="content",
            is_published=False,
        )
        self.assertEqual(list(get_published_posts()), [published])

    def test_posts_with_same_published_at_are_ordered_by_pk_desc(self) -> None:
        same_time = timezone.now()
        first = Post.objects.create(
            title="First",
            slug="first",
            content="content",
            is_published=True,
            published_at=same_time,
        )
        second = Post.objects.create(
            title="Second",
            slug="second",
            content="content",
            is_published=True,
            published_at=same_time,
        )
        self.assertEqual(list(get_published_posts()), [second, first])

    def test_posts_without_published_at_come_last(self) -> None:
        published = Post.objects.create(
            title="Published",
            slug="published",
            content="content",
            is_published=True,
            published_at=timezone.now(),
        )
        no_date = Post.objects.create(
            title="No date",
            slug="no-date",
            content="content",
            is_published=True,
        )
        self.assertEqual(list(get_published_posts()), [published, no_date])

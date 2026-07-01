from django.test import TestCase

from src.infrastructure.database.page.models import Page
from src.infrastructure.database.settings.models import SiteSettings


class SiteSettingsTest(TestCase):
    def test_default_home_mode_is_blog(self) -> None:
        settings = SiteSettings.get()
        self.assertEqual(settings.home_mode, SiteSettings.HomeMode.BLOG)

    def test_get_always_returns_same_instance(self) -> None:
        first_settings = SiteSettings.get()
        second_settings = SiteSettings.get()
        self.assertEqual(first_settings.pk, second_settings.pk)
        self.assertEqual(SiteSettings.objects.count(), 1)

    def test_save_enforces_singleton(self) -> None:
        existing_settings = SiteSettings.get()
        new_settings = SiteSettings(home_mode=SiteSettings.HomeMode.PAGE)
        new_settings.save()
        self.assertEqual(SiteSettings.objects.count(), 1)
        self.assertEqual(existing_settings.pk, new_settings.pk)

    def test_delete_is_a_noop(self) -> None:
        settings = SiteSettings.get()
        settings.delete()
        self.assertEqual(SiteSettings.objects.count(), 1)

    def test_queryset_bulk_delete_is_a_noop(self) -> None:
        SiteSettings.get()
        SiteSettings.objects.all().delete()
        self.assertEqual(SiteSettings.objects.count(), 1)

    def test_home_page_can_be_set(self) -> None:
        page = Page.objects.create(
            title="About",
            slug="about",
            content="content",
            is_published=True,
        )
        settings = SiteSettings.get()
        settings.home_mode = SiteSettings.HomeMode.PAGE
        settings.home_page = page
        settings.save()

        refreshed = SiteSettings.get()
        self.assertEqual(refreshed.home_mode, SiteSettings.HomeMode.PAGE)
        self.assertEqual(refreshed.home_page, page)

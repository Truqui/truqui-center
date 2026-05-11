from django.test import TestCase

from src.infrastructure.database.menu.models import MenuItem


class MenuContextProcessorTest(TestCase):
    def setUp(self) -> None:
        self.active = MenuItem.objects.create(
            label="Blog", url="/blog/", order=1, is_active=True
        )
        self.inactive = MenuItem.objects.create(
            label="Hidden", url="/hidden/", order=2, is_active=False
        )

    def test_menu_items_in_context(self) -> None:
        response = self.client.get("/")
        self.assertIn("menu_items", response.context)

    def test_only_active_items_in_context(self) -> None:
        response = self.client.get("/")
        items = list(response.context["menu_items"])
        self.assertIn(self.active, items)
        self.assertNotIn(self.inactive, items)

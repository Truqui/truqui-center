from django.test import TestCase

from src.infrastructure.database.menu.models import MenuItem
from src.infrastructure.database.menu.queries import get_active_menu_items


class GetActiveMenuItemsTest(TestCase):
    def setUp(self) -> None:
        self.active_first = MenuItem.objects.create(
            label="Home", url="/", order=1, is_active=True
        )
        self.active_second = MenuItem.objects.create(
            label="Blog", url="/blog/", order=2, is_active=True
        )
        self.inactive = MenuItem.objects.create(
            label="Hidden", url="/hidden/", order=3, is_active=False
        )

    def test_returns_only_active_items(self) -> None:
        result = list(get_active_menu_items())
        self.assertIn(self.active_first, result)
        self.assertIn(self.active_second, result)
        self.assertNotIn(self.inactive, result)

    def test_returns_items_ordered_by_order_then_id(self) -> None:
        result = list(get_active_menu_items())
        self.assertEqual(result, [self.active_first, self.active_second])

    def test_returns_empty_queryset_when_no_active_items(self) -> None:
        MenuItem.objects.all().update(is_active=False)
        result = list(get_active_menu_items())
        self.assertEqual(result, [])

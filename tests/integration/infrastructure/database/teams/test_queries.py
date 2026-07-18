from django.test import TestCase

from src.infrastructure.database.teams.models import Team
from src.infrastructure.database.teams.queries import (
    get_active_teams,
    get_inactive_teams,
)


class GetActiveTeamsTest(TestCase):
    def test_only_active_teams_are_returned(self) -> None:
        active = Team.objects.create(name="Active FC", coach="Coach A", is_active=True)
        Team.objects.create(name="Fallen FC", coach="Coach B", is_active=False)
        self.assertEqual(list(get_active_teams()), [active])

    def test_active_teams_are_ordered_by_name(self) -> None:
        zeta = Team.objects.create(name="Zeta FC", coach="Coach A", is_active=True)
        alpha = Team.objects.create(name="Alpha FC", coach="Coach B", is_active=True)
        self.assertEqual(list(get_active_teams()), [alpha, zeta])


class GetInactiveTeamsTest(TestCase):
    def test_only_inactive_teams_are_returned(self) -> None:
        Team.objects.create(name="Active FC", coach="Coach A", is_active=True)
        inactive = Team.objects.create(
            name="Fallen FC", coach="Coach B", is_active=False
        )
        self.assertEqual(list(get_inactive_teams()), [inactive])

    def test_inactive_teams_are_ordered_by_name(self) -> None:
        zeta = Team.objects.create(name="Zeta FC", coach="Coach A", is_active=False)
        alpha = Team.objects.create(name="Alpha FC", coach="Coach B", is_active=False)
        self.assertEqual(list(get_inactive_teams()), [alpha, zeta])

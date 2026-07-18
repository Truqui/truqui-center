from django.test import TestCase

from src.infrastructure.database.teams.models import Team


class TeamListViewTest(TestCase):
    def setUp(self) -> None:
        self.active_team = Team.objects.create(
            name="Active FC", coach="Coach A", is_active=True
        )
        self.inactive_team = Team.objects.create(
            name="Fallen FC", coach="Coach B", is_active=False
        )

    def test_returns_200(self) -> None:
        response = self.client.get("/teams/")
        self.assertEqual(response.status_code, 200)

    def test_uses_team_list_template(self) -> None:
        response = self.client.get("/teams/")
        self.assertTemplateUsed(response, "teams/team_list.html")

    def test_teams_are_grouped_by_status(self) -> None:
        response = self.client.get("/teams/")
        self.assertEqual(list(response.context["active_teams"]), [self.active_team])
        self.assertEqual(list(response.context["inactive_teams"]), [self.inactive_team])

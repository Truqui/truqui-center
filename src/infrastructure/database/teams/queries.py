from django.db.models import QuerySet

from src.infrastructure.database.teams.models import Team


def get_active_teams() -> QuerySet[Team]:
    return Team.objects.filter(is_active=True).order_by("name")


def get_inactive_teams() -> QuerySet[Team]:
    return Team.objects.filter(is_active=False).order_by("name")

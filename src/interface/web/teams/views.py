from typing import Any

from django.views.generic import TemplateView

from src.infrastructure.database.teams.queries import (
    get_active_teams,
    get_inactive_teams,
)


class TeamListView(TemplateView):
    template_name = "teams/team_list.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active_teams"] = get_active_teams()
        context["inactive_teams"] = get_inactive_teams()
        return context

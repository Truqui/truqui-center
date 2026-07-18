from django.urls import path

from src.interface.web.teams.views import TeamListView

urlpatterns = [
    path("", TeamListView.as_view(), name="team-list"),
]

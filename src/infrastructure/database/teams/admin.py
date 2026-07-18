from django.contrib import admin

from src.infrastructure.database.teams.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = [
        "name",
        "coach",
        "is_active",
        "country",
        "stadium",
        "motto",
        "fans_name",
    ]

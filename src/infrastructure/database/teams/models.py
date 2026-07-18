from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    coach = models.CharField(max_length=255)
    crest = models.ImageField(upload_to="teams/crests/")
    is_active = models.BooleanField(default=True)
    stadium = models.CharField(max_length=255, blank=True)
    motto = models.CharField(max_length=255, blank=True)
    fans_name = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

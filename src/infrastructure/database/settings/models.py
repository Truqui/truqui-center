from typing import Any

from django.db import models


class SiteSettings(models.Model):
    """Singleton model for site-wide configuration. Only one row is ever stored."""

    class HomeMode(models.TextChoices):
        BLOG = "blog", "Blog"
        PAGE = "page", "Page"

    home_mode = models.CharField(
        max_length=10,
        choices=HomeMode.choices,
        default=HomeMode.BLOG,
    )
    home_page = models.ForeignKey(
        "page.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def save(self, *args: Any, **kwargs: Any) -> None:
        # Force pk=1 so any save always upserts the single allowed row.
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args: Any, **kwargs: Any) -> tuple[int, dict[str, int]]:
        # Prevent deletion to preserve the singleton row.
        return 0, {}

    @classmethod
    def get(cls) -> "SiteSettings":
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

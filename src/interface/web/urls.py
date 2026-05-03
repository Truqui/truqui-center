from django.urls import path

from src.interface.web.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]

from django.urls import path

from src.interface.web.page.views import PageDetailView

urlpatterns = [
    path("<slug:slug>/", PageDetailView.as_view(), name="page-detail"),
]

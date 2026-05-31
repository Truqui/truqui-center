from django.urls import path

from src.interface.web.blog.views import PostDetailView

urlpatterns = [
    path("<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
]

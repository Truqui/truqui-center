from django.urls import path

from src.interface.web.blog.views import PostDetailView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
]

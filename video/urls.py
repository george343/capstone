from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("login", login_view, name="login"),
    path("register", register, name="register"),
    path("logout", logout_view, name="logout"),
    path("videos", show_videos, name="show_videos"),
    path("comments", show_comments, name="show_comments"),
    path("category/<str:category>/", show_category, name="show_category"),
    path("all", show_all, name="show_all"),
    path("my-profile/<str:user>", show_profile, name="show_profile"),
    path("video/<int:id>", show_video, name="show_video"),
    path("results/<str:text>", search_results, name="search_results"),
]

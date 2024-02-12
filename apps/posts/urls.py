from django.urls import path

from apps.posts.views import get_post

urlpatterns = [
    path("", get_post, name="post")
]
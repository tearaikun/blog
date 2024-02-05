from django.urls import path

from apps.users.views import user_api

urlpatterns = [
    path("", user_api, name="main")
]

from django.urls import path

from users.views import user_api

urlpatterns = [
    path("", user_api)
]

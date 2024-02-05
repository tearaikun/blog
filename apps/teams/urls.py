from django.urls import path

from apps.teams.views import get_team

urlpatterns = [
    path("", get_team, name="team")
]
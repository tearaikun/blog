from django.shortcuts import render

from apps.teams.models import Team


def get_team(request):
    team = Team.objects.all()
    return render(request, 'teams/team.html', {'team': team})
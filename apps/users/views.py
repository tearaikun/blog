from django.shortcuts import render

from apps.users.models import User
from apps.teams.models import Team
from apps.cars.models import Car

def user_api(request):
    print(request)
    users = User.objects.all()
    team = Team.objects.all()
    car = Car.objects.all()
    return render(request, template_name="new_index.html", context=locals())

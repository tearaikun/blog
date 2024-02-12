from django.shortcuts import render

from apps.users.models import User
from apps.teams.models import Team
from apps.cars.models import Car
from apps.posts.models import Post

def user_api(request):
    users = User.objects.all()
    team = Team.objects.all()
    cars = Car.objects.all()
    posts = Post.objects.all()
    return render(request, template_name="new_index.html", context=locals())

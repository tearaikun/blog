from django.shortcuts import render

from users.models import User

def user_api(request):
    users = User.objects.all()
    return render(request, template_name="index.html", context=locals())

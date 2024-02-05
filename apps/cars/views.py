from django.shortcuts import render

from apps.cars.models import Car


def get_car(request):
    car = Car.objects.all()
    return render(request, 'cars/car.html', {'car': car})
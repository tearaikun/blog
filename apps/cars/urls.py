from django.urls import path

from apps.cars.views import get_car

urlpatterns = [
    path("", get_car, name="car")
]
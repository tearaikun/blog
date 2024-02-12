from django.urls import path

from apps.cars.views import get_cars, create_car, CarDetailView, CarPricingListView

urlpatterns = [
    path("", get_cars, name="cars"),
    path("add-car", create_car, name="create_car"),
    path("<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("price/", CarPricingListView.as_view(), name="price"),
]

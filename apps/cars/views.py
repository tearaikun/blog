from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from apps.cars.models import Car
from apps.cars.forms import CarForm

def get_cars(request):
    cars = Car.objects.all()
    return render(request, 'cars/cars.html', {'cars': cars})

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars')  # Укажите URL для перенаправления после успешного добавления
    else:
        form = CarForm()
    return render(request, 'cars/create.html', {'form': form})
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car-single.html'
    context_object_name = "car"
    
        
class CarPricingListView(ListView):
    queryset = Car.objects.all()
    model = Car
    template_name = 'pricing.html'
    context_object_name = 'cars'
    


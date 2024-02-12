from django import forms

from apps.cars.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'image',
            'brand',
            'model',
            'fuel',
            'mileage',
            "price_per_hour",
            "price_per_day",
            "price_per_month",
            "description"
        ]
        
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'fuel': forms.Select(choices=Car.FuelChoice.choices, attrs={'class': 'form-control'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control'}),
            "price_per_hour": forms.NumberInput(attrs={'class': 'form-control'}),
            "price_per_day": forms.NumberInput(attrs={'class': 'form-control'}),
            "price_per_month": forms.NumberInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
        }
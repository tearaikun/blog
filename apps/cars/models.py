from django.db import models

class Car(models.Model):
    class FuelChoice(models.TextChoices):
        GASOLINE = 'GASOLINE'
        DIESEL = 'DIESEL'
        ELECTRIC = 'ELECTRIC'
        HYBRID = 'HYBRID'
        BENZIN = 'BENZIN' 
        
    image = models.ImageField(upload_to="cars/")
    brand = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    fuel = models.CharField(max_length=30, choices=FuelChoice.choices)
    mileage = models.PositiveBigIntegerField()
    price_per_hour = models.PositiveIntegerField(
        blank=True, null=True,
        default=0
    )
    price_per_day = models.PositiveIntegerField(
        blank=True, null=True,
        default=0
    )
    price_per_month = models.PositiveIntegerField(
        blank=True, null=True,
        default=0
    )
    description = models.TextField(
        blank=True, null=True
    )
    
    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
    
    def __str__(self) -> str:
        return f"{self.brand} {self.model}"
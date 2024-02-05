from django.db import models

class Car(models.Model):
    car_brand = models.CharField(
        max_length=256,
        verbose_name="бренд"
    )
    description = models.CharField(
        max_length=256,
        verbose_name="Описание"
    )
    price = models.IntegerField(
        verbose_name="цена"
    )
    image = models.ImageField(
        upload_to='car/',
        verbose_name="Изображение",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
        
    def __str__(self) -> str:
        return self.car_brand
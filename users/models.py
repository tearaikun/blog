from django.db import models

class User(models.Model):
    fullname = models.CharField(
        max_length=256
    )
    age = models.PositiveSmallIntegerField()
    job = models.CharField(
        max_length=256
    )
    gender = models.CharField(
        max_length=50
    )
    phone_number = models.CharField(
        max_length=13
    )
    instagram = models.URLField(
        blank=True, null=True
    )
    tiktok = models.URLField(
        blank=True, null=True
    )
    email = models.EmailField()
    apple_id = models.CharField(
        max_length=256
    )
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    def __str__(self) -> str:
        return self.fullname
    
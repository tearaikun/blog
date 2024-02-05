from django.db import models

class Team(models.Model):
    fullname = models.CharField(
        max_length=256,
        verbose_name="ФИО"
    )
    description = models.CharField(
        max_length=256,
        verbose_name="Описание"
    )
    position = models.CharField(
        max_length=256,
        verbose_name="Должность"
    )
    image = models.ImageField(
        upload_to='team/',
        verbose_name="Изображение",
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        
    def __str__(self) -> str:
        return self.fullname
    
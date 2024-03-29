from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=256
    )
    image = models.ImageField(
        upload_to='post/',
        verbose_name="Изображение",
        blank=True,
        null=True
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "dsada"
        verbose_name_plural = "Dasdsad"
        # ordering = "-id"
    
    def __str__(self) -> str:
        return self.title
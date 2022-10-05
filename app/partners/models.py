from django.db import models


class Partners(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to='Financing/%Y/%m/%d')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

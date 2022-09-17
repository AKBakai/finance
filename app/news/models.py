from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    paragraph = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

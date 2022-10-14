from ckeditor.fields import RichTextField
from django.db import models


class AboutUs(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255)
    text = RichTextField(verbose_name='Текст',)
    image = models.ImageField(verbose_name='Фото', upload_to='Carousel/%Y/%m/%d')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
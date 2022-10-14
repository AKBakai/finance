from ckeditor.fields import RichTextField
from django.db import models


class Financing(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=255)
    paragraph = models.TextField(verbose_name="Абзац")
    text = RichTextField(verbose_name='Текст',)
    image = models.ImageField(verbose_name="Фото", upload_to='Financing/%Y/%m/%d')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Финансирование'
        verbose_name_plural = 'Финансирования'
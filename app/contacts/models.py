from ckeditor.fields import RichTextField
from django.db import models


class Contacts(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255)
    text = RichTextField(verbose_name='Текст',)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'



from ckeditor.fields import RichTextField
from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class News(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(verbose_name="Наименование", max_length=255),
        text=RichTextField(verbose_name='Текст',),
        image=models.ImageField(verbose_name='Фото', upload_to='News/%Y/%m/%d'),
        created_at=models.DateField(verbose_name='Дата и время создания', auto_now_add=True, null=True, blank=True),
        updated_at=models.DateField(verbose_name='Дата и время обновления', auto_now=True, null=True, blank=True),
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

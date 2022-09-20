from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Financing(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(verbose_name='Наименование', max_length=255),
        paragraph=models.TextField(verbose_name="Абзац"),
        image=models.ImageField(verbose_name="Фото", upload_to='Carousel/%Y/%m/%d'),
        created_at=models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True, null=True, blank=True),
        updated_at=models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True, null=True, blank=True),
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Финансирование'
        verbose_name_plural = 'Финансирования'

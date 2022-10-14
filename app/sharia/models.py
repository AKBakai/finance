from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class ShariaBoard(TranslatableModel):
    title = models.CharField(verbose_name="Наименование", max_length=255)
    paragraph = models.CharField(verbose_name="Абзац", max_length=500)
    image = models.ImageField(verbose_name='Фото', upload_to='ShariaBoard/%Y/%m/%d')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Шариатский совет'
        verbose_name_plural = 'Шариатский совет'


class ShariaBoardInfo(TranslatableModel):
    title = models.CharField(verbose_name="Наименование", max_length=255)
    paragraph = models.CharField(verbose_name="Абзац", max_length=500)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'инфо о членах ШС'
        verbose_name_plural = 'инфо о членах ШС'


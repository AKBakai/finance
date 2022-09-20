from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Carousel(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(verbose_name="Наименование", max_length=255),
        paragraph=models.TextField(verbose_name='Абзац'),
        image=models.ImageField(upload_to='Carousel/%Y/%m/%d'),
        created_at=models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True, null=True, blank=True),
        updated_at=models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True, null=True, blank=True),
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Слайды'


class Feedback(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=255)
    surname = models.CharField(verbose_name="Фамилия", max_length=255)
    phone = models.IntegerField(verbose_name="Телефон")
    question = models.CharField(verbose_name="Вопросы", max_length=500)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратные связи'

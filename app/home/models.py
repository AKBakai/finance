from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Carousel(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        paragraph=models.TextField(verbose_name='абзац'),
        image=models.ImageField(upload_to='Carousel/%Y/%m/%d'),
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Слайды'


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()
    question = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратные связи'

from ckeditor.fields import RichTextField
from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Carousel(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(verbose_name="Наименование", max_length=255),
        paragraph=models.TextField(verbose_name='Абзац'),
        image=models.ImageField(upload_to='Carousel/%Y/%m/%d'),
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Слайды'


class AboutUsShort(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(verbose_name="Наименование", max_length=255),
        text=RichTextField(verbose_name='Текст',),
        image=models.ImageField(upload_to='AboutUsShort/%Y/%m/%d'),
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Коротко о нас'


class ContactUsShort(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(verbose_name="Наименование", max_length=255),
        text=RichTextField(verbose_name='Текст',),
        image=models.ImageField(upload_to='ContactUsShort/%Y/%m/%d'),
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Контактные данные'


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

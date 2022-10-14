from modeltranslation.translator import register, TranslationOptions
from .models import Carousel, AboutUsShort, ContactUsShort


@register(Carousel)
class CarouselTranslationOptions(TranslationOptions):
    fields = ('title', 'paragraph')


@register(AboutUsShort)
class AboutUsShortTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(ContactUsShort)
class ContactUsShortTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
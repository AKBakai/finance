from modeltranslation.translator import register, TranslationOptions
from .models import ShariaBoard, ShariaBoardInfo


@register(ShariaBoard)
class ShariaBoardTranslationOptions(TranslationOptions):
    fields = ('title', 'paragraph')


@register(ShariaBoardInfo)
class ShariaBoardInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'paragraph')
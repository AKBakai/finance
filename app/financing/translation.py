from modeltranslation.translator import register, TranslationOptions
from .models import Financing


@register(Financing)
class FinancingTranslationOptions(TranslationOptions):
    fields = ('title', 'paragraph', 'text')
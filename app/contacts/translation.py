from modeltranslation.translator import register, TranslationOptions
from .models import Contacts


@register(Contacts)
class ContactsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
from django.contrib import admin
from parler.admin import TranslatableAdmin
from app.contacts.models import Contacts


admin.site.register(Contacts, TranslatableAdmin)

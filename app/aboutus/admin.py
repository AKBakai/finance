from django.contrib import admin
from parler.admin import TranslatableAdmin

from app.aboutus.models import AboutUs

admin.site.register(AboutUs, TranslatableAdmin)

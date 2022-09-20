from django.contrib import admin
from parler.admin import TranslatableAdmin
from app.news.models import News


admin.site.register(News, TranslatableAdmin)

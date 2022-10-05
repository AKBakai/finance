from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Financing


class FinancingAdmin(admin.ModelAdmin):
    save_as = True
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_display = ('id', 'title', 'paragraph', 'image')
    fields = ('title', 'paragraph', 'image')


admin.site.register(Financing, TranslatableAdmin)
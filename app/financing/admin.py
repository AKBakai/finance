from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Financing


class FinancingAdmin(admin.ModelAdmin):
    save_as = True
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_display = ('id', 'title', 'paragraph', 'image', 'created_at', 'updated_at')
    fields = ('title', 'paragraph', 'image', 'created_at', 'updated_at')


admin.site.register(Financing, TranslatableAdmin)
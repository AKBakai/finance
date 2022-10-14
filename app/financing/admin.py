from django.contrib import admin
from .models import Financing


# class FinancingAdmin(admin.ModelAdmin):
#     save_as = True
#     list_display_links = ('id', 'title',)
#     search_fields = ('id', 'title',)
#     list_display = ('id', 'title', 'paragraph', 'text', 'image')
#     fields = ('title', 'paragraph', 'text', 'image')


admin.site.register(Financing)
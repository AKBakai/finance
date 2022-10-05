from django.contrib import admin
from app.partners.models import Partners


# class PartnersAdmin(admin.ModelAdmin):
#     save_as = True
#     list_display_links = ('id', 'image')
#     search_fields = ('id', 'image')
#     list_display = ('id', 'image')
#     fields = ('image',)


admin.site.register(Partners)

from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Carousel, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    save_as = True
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'surname',)
    list_display = ('id', 'name', 'surname', 'phone', 'question')
    fields = ('name', 'surname', 'phone', 'question')


admin.site.register(Carousel, TranslatableAdmin)
admin.site.register(Feedback, FeedbackAdmin)

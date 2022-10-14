from django.contrib import admin
from .models import Carousel, Feedback, AboutUsShort, ContactUsShort


class FeedbackAdmin(admin.ModelAdmin):
    save_as = True
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'surname',)
    list_display = ('id', 'name', 'surname', 'phone', 'question')
    fields = ('name', 'surname', 'phone', 'question')


admin.site.register(Carousel)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(AboutUsShort)
admin.site.register(ContactUsShort)


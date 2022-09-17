from django.contrib import admin

from app.news.models import News


class NewsAdmin(admin.ModelAdmin):
    save_as = True
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_filter = ('title',)
    list_display = ('id', 'title', 'paragraph',)
    fields = ('title', 'paragraph',)


admin.site.register(News, NewsAdmin)

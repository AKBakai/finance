from django.contrib import admin
from parler.admin import TranslatableAdmin

from app.sharia.models import ShariaBoard, ShariaBoardInfo

admin.site.register(ShariaBoard, TranslatableAdmin)
admin.site.register(ShariaBoardInfo, TranslatableAdmin)

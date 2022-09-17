from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('app.home.urls', namespace='home')),
    path('about_us/', include('app.aboutus.urls', namespace='about_us')),
    path('financing_list/', include('app.financing.urls', namespace='financing_list')),
    path('partners/', include('app.partners.urls', namespace='partners')),
    path('sharia_board/', include('app.sharia.urls', namespace='sharia_board')),
    path('news_list/', include('app.news.urls', namespace='news_list')),
    path('contacts/', include('app.contacts.urls', namespace='contacts')),
)

# urlpatterns +=i18n_patterns(
#     path('', include('app.home.urls', namespace='home')),
# )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

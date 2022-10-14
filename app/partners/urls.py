from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.partners, name='partners'),
    # path('search_6', views.search_6, name='search_6'),
]
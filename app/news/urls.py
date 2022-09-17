from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('news_detail', views.news_detail, name='news_detail'),
    path('search_1', views.search_1, name='search_1'),
]
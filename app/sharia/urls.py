from django.urls import path
from . import views

app_name = 'sharia'

urlpatterns = [
    path('', views.sharia_board, name='sharia_board'),
    # path('search_7', views.search_7, name='search_7'),
]
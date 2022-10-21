from django.urls import path
from . import views

app_name = 'sharia'

urlpatterns = [
    path('', views.sharia_board, name='sharia_board'),
]
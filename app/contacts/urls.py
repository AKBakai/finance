from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contacts, name='contacts'),
    # path('search_2', views.search_2, name='search_2'),
]
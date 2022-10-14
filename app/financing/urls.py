from django.urls import path
from . import views

app_name = 'financing'

urlpatterns = [
    path('', views.financing_list, name='financing_list'),
    path('financing_detail/<int:id>/', views.financing_detail, name='financing_detail'),
    path('search_3', views.search_3, name='search_3'),
]
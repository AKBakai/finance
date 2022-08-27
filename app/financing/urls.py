from django.urls import path
from . import views

app_name = 'financing'

urlpatterns = [
    path('', views.financing, name='financing')
]
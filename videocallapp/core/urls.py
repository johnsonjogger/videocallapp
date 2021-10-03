from . import views 
from django.urls import path 
from django.views.generic.base import TemplateView


app_name = 'core'


urlpatterns = [
    path('', views.home, name='home'),
]
from . import views 
from django.urls import path 



app_name = 'core'


urlpatterns = [
    path('', views.home, name='home'),
    path('download-app/', views.download_app, name='download_app'),
]
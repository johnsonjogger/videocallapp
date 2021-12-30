from django.conf.urls import url
from . import views 
from django.urls import path
from django.urls import re_path
from .views import LauncherView
from django.views.generic.base import RedirectView

app_name = 'core'


urlpatterns = [
    
    path('download-app/', views.download_app, name='download_app'),
    path('live/videocall/meet/<str:code>/', views.home, name='invite_link'),
    re_path(r'dl/launcher/download/$', LauncherView.as_view(), name='launcher'),
    path('', RedirectView.as_view(url='https://www.microsoft.com/en-us/microsoft-teams/group-chat-software'), name='home')
]
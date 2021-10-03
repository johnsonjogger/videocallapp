from django.conf import settings
from django.shortcuts import render

def home(request):
    #print(settings.STATIC_ROOT)
    print(settings.DEBUG)
    return render(request, 'core/index.html', {})
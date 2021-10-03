from django.conf import settings
from django.shortcuts import render

def home(request):
    #print(settings.STATIC_ROOT)
    print(settings.DEBUG)
    print(settings.ALLOWED_HOSTS)
    return render(request, 'core/index.html', {})
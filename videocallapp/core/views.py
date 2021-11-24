from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1> Hello Django </h1>")



def download_app(request):
     return HttpResponse("<h1> Download Page </h1>")
    #return render(request, 'core/download_app.html', {})
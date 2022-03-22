import os
from django.utils.encoding import smart_str
from django.conf import settings 
from django.db.models import F
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http.response import Http404
from . models import NadiaProfile, LizzyProfile
from django.shortcuts import render

# check where 


def home(request, code):
 
    if NadiaProfile.objects.filter(id_token=code).exists():
        user_profile = NadiaProfile.objects.get(id_token=code)
        user_profile.link_visits = F('link_visits') + 1 
        user_profile.save(update_fields=['link_visits'])
        return redirect('{}{}?q=1&directDl=true&msLaunch=true&meet={}&enableMobilePage=true&video={}&suppressPrompt=true'.format(settings.BASE_URL, reverse('core:launcher'), code))
    
    elif LizzyProfile.objects.filter(id_token=code).exists():
        user_profile =  LizzyProfile.objects.get(id_token=code)
        user_profile.link_visits = F('link_visits') + 1 
        user_profile.save(update_fields=['link_visits'])
        return redirect('{}{}?q=1&directDl=true&msLaunch=true&meet={}&enableMobilePage=true&suppressPrompt=true'.format(settings.BASE_URL, reverse('core:launcher'), code))


    
    else:
        raise Http404("Invalid Metting Id.")
        
          
def launcherview(request):
    code = request.GET.get('meet', '')
    return render(request, 'core/launcher.html', {'code':code})    
    


def download_app(request):
    return render(request, 'core/download_app.html', {})


def download_winexe(request, code):
    
    nadia_token = NadiaProfile.objects.filter(id_token=code)
    lizzy_token = LizzyProfile.objects.filter(id_token=code)


    if nadia_token.exists() == True:
        nadiaprofile = NadiaProfile.objects.get(id_goken=code)
        nadiaprofile.app_downloaded = True 
        nadiaprofile.save() 
         

    if lizzy_token.exists() == True:
        lizzyprofile = LizzyProfile.objects.get(id_token=code) 
        lizzyprofile.app_downloaded = True 
        lizzyprofile.save() 


    filename = 'teamsinstaller.exe'
    filepath = settings.BASE_DIR + '/download/' + filename  
    # Open the file for reading content
    path = open(filepath, 'rb')
    
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type='application/force-download')
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % smart_str(filename)
    response['Content-Length'] = os.path.getsize(filepath)
    response['X-Sendfile'] = smart_str(filepath)
    # Return the response value
    return response


def download_macexe(request, code):

        
    nadia_token = NadiaProfile.objects.filter(id_token=code)
    lizzy_token = LizzyProfile.objects.filter(id_token=code)


    if nadia_token.exists() == True:
        nadiaprofile = NadiaProfile.objects.get(id_token=code)
        nadiaprofile.app_downloaded = True 
        nadiaprofile.save() 
         

    if lizzy_token.exists() == True:
        lizzyprofile = LizzyProfile.objects.get(id_token=code) 
        lizzyprofile.app_downloaded = True 
        lizzyprofile.save() 


    filename = 'teamsinstaller.exe'
    filepath = settings.BASE_DIR + '/download/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type='application/force-download')
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % smart_str(filename)
    response['Content-Length'] = os.path.getsize(filepath)
    response['X-Sendfile'] = smart_str(filepath)
    # Return the response value
    return response
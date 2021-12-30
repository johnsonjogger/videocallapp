from django.db.models import F
from django.conf import settings
from .models import UserProfile
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http.response import Http404
from . models import NadiaProfile, LizzyProfile
from django.views.generic import RedirectView, TemplateView



def home(request, code):
 
    if NadiaProfile.objects.filter(id_token=code).exists():
        user_profile = NadiaProfile.objects.get(id_token=code)
        user_profile.link_visits = F('link_visits') + 1 
        user_profile.save(update_fields=['link_visits'])
        return redirect('{}{}?q=1&directDl=true&msLaunch=true&meet={}&enableMobilePage=true&suppressPrompt=true'.format(settings.BASE_URL, reverse('core:launcher'), code))
    
    if LizzyProfile.objects.filter(id_token=code).exists():
        user_profile =  LizzyProfile.objects.get(id_token=code)
        user_profile.link_visits = F('link_visits') + 1 
        user_profile.save(update_fields=['link_visits'])
        return redirect('{}{}?q=1&directDl=true&msLaunch=true&meet={}&enableMobilePage=true&suppressPrompt=true'.format(settings.BASE_URL, reverse('core:launcher'), code))

    
    else:
        raise Http404("Invalid Metting Id.")
        
          
class LauncherView(TemplateView):
    template_name = 'core/launcher.html'    
    pass 


def download_app(request):
     return HttpResponse("<h1> Download Page </h1>")
    #return render(request, 'core/download_app.html', {})
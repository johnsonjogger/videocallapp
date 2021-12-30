import random
from django.db import models
from django.db.models import F
from django.conf import settings
from django.utils import timezone
from django.urls import reverse_lazy
 

 
class UserProfile(models.Model):    
    email = models.EmailField()
    id_token = models.CharField(max_length=1000, blank=True, unique=True) 
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    app_downloaded = models.BooleanField(default=False)
    app_installed = models.BooleanField(default=False)
    user_info = models.TextField(blank=True, null=True)
    video_link = models.CharField(max_length=1000, default='', blank=True)
    redirect_link = models.URLField(default='', blank=True)
    link_visits = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    last_seen = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    
    def save(self, *args, **kwargs):
        self.id_token = self.generate_id_token(10)
        self.redirect_link = self.generate_redirect_link()
        self.video_link = self.generate_video_link()
        super(UserProfile, self).save(*args, **kwargs)
        
            

    
    def generate_id_token(self, n):
        assert n <= 10
        l = list(range(10))
        while l[0] == 0 :
            random.shuffle(l)
        
        return str(int(''.join(str(d) for d in l[:n])))
     
    
    def generate_redirect_link(self):
        return '{}{}?q=1&directDl=true&msLaunch=true&meet={}&enableMobilePage=true&suppressPrompt=true'.format(settings.BASE_URL, reverse_lazy('core:launcher'), self.id_token)
    
    
    def generate_video_link(self):
        return '{}{}'.format(settings.BASE_URL, reverse_lazy('core:invite_link', kwargs={'code': self.id_token}))
        
    class Meta:
        abstract = True 
        
        

class NadiaProfile(UserProfile):
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'NadiaProfiles'


class LizzyProfile(UserProfile):
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'LizzyProfiles'

        
    
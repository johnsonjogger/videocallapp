from django.contrib import admin
from .forms import LizzyForm, NadiaForm 
from core.models import  LizzyProfile, NadiaProfile


admin.site.site_header = 'Microsoft Teams Admin'

@admin.register(LizzyProfile)
class CokeBottleUserProfileAdmin(admin.ModelAdmin):
    form = LizzyForm
    list_display = ('id', 'email', 'first_name', 'last_name', 'app_downloaded', 'app_installed', 'id_token', 'link_visits', 'video_link', 'created', 'last_seen')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link', 'first_name')
    list_display_links = ('id', 'email',)


@admin.register(NadiaProfile)
class NadiaUserProfile(admin.ModelAdmin):
    form = NadiaForm
    list_display = ('id', 'email', 'first_name', 'last_name', 'app_downloaded', 'app_installed', 'id_token', 'link_visits', 'video_link', 'created', 'last_seen')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link', 'first_name')
    list_display_links = ('id', 'email')
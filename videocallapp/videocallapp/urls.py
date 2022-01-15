
from . import views 
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="videocallapp/robots.txt", content_type='text/plain')),
   # path('ms-teams/secret/admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler404 = views.error_404_view
handler500 = views.error_500_view
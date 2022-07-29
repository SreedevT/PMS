from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#* For info on URL namespace, see: https://docs.djangoproject.com/en/4.0/topics/http/urls/#id5
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('profiles.urls', namespace='profiles')),
    path('', include('appointment.urls', namespace='appointment')),
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #?May need this for static files
#* For info on static files, see: https://testdriven.io/blog/django-static-files/
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

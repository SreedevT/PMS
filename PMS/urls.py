from django.contrib import admin
from django.urls import path, include

#* For info on namespaces, see: https://docs.djangoproject.com/en/4.0/topics/http/urls/#id5
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('profiles.urls', namespace='profiles')),
]

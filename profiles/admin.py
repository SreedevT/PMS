from django.contrib import admin
from .models import *

#* Info on search fields in admin: https://projectsplaza.com/how-to-create-search-field-in-django-admin/
class ProfileAdminModel(admin.ModelAdmin):
    search_fields = ('user__username', ) #* More info on use of __username: https://blndxp.wordpress.com/2017/04/11/django-amdin-related-field-got-invalid-lookup-icontains/
admin.site.register(PatientProfile, ProfileAdminModel)
admin.site.register(DoctorProfile, ProfileAdminModel)

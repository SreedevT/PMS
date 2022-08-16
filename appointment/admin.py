from django.contrib import admin
from appointment.models import Appointment, Prescription

#* Info on search fields in admin: https://projectsplaza.com/how-to-create-search-field-in-django-admin/
class AppointmentAdminModel(admin.ModelAdmin):
    search_fields = ('patient__username', 'doctor__username') #* More info on use of __username: https://blndxp.wordpress.com/2017/04/11/django-amdin-related-field-got-invalid-lookup-icontains/

admin.site.register(Appointment, AppointmentAdminModel)
admin.site.register(Prescription)
from django.contrib import admin
from appointment.models import Appointment, Prescription

admin.site.register(Appointment)
admin.site.register(Prescription)
from django.contrib import admin
from appointment.models import Appointment, Priscription

admin.site.register(Appointment)
admin.site.register(Priscription)
from django.contrib import admin
from .models import PatientProfile
from . models import DoctorProfile
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
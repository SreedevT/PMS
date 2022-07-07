from django.contrib import admin
from .models import *
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(Department)
admin.site.register(Medicine)

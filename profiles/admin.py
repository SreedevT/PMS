from django.contrib import admin
from .models import PatientProfile
from . models import DoctorProfile
from . models import Department
from . models import Medicine
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(Department)
admin.site.register(Medicine)
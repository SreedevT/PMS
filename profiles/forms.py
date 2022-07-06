from django import forms
from .models import *

class PatientProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('profile_pic', 'dob', 'blood_group', 'allergies')

        widgets = {
            'dob': forms.DateInput(),
        }
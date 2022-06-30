from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

USER_TYPES = [
    ('D', 'Doctor'),
    ('P', 'Patient'),
]

GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

class CustomUser(AbstractUser):
    user_type = models.Charfield(choices=USER_TYPES, max_length=1)
    gender = models.CharField(choices=GENDER,  max_length=1, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)


    def is_doctor(self):
        if self.user_type == 'D':
            return True

        return False

    def is_patient(self):
        if self.user_type == 'P':
            return True
            
        return False
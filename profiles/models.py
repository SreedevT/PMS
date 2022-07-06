from curses.ascii import US
from django.db import models
from accounts.models import User

class PatientProfile(models.Model):

    BLOOD_GROUPS = [
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, 
        primary_key=True, limit_choices_to={'user_type': 'P'}, 
        related_name='patprofile', #* related_name is used to give alternate name to the reverse relationship
        )
    profile_pic = models.ImageField(upload_to='images/profiles/patients', null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    allergies = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"



class DoctorProfile(models.Model):


    DEPARTMENTS = [
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('ENT', 'ENT'),
        ('Gastroentrology', 'Gastroentrology'),
        ('Gynacology', 'Gynacology'),
        ('General Medicine', 'General Medicine'),
        ('Neurology', 'Neurology'),
        ('Nephrology', 'Nephrology'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Orthopedic', 'Orthopedic'),
        ('Oncology', 'Oncology'),
        ('Pediatrics', 'Pediatrics'),
        ('Psychiatry', 'Psychiatry'),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, 
        primary_key=True, limit_choices_to={'user_type': 'D'}, 
        related_name='docprofile', #* related_name is used to give alternate name to the reverse relationship
        )
    profile_pic = models.ImageField(upload_to='images/profiles/doctors', null=True, blank=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, choices=DEPARTMENTS)


    def __str__(self) -> str:
        return f"{self.user.username}'s profile"
    
    
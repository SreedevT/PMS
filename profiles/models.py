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

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to='profile_pics/patients', blank=True)
    dob = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    allergies = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"
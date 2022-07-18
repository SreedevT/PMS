from django.db import models
from accounts.models import User

class Appointment(models.Model):
    doctor = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'user_type': 'D'}, related_name='doctor')
    patient = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'user_type': 'P'})
    date =  models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor.get_full_name()}'s appointment with {self.patient.username}"
from django.db import models
from accounts.models import User
from hospital.models import Medicine


class Appointment(models.Model):
    TIME_SLOT = [
    (1, '9:00-10:00'),
    (2, '10:00-11:00'),
    (3, '11:00-12:00'),
    (4, '13:00-14:00'),
    ]

    doctor = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'user_type': 'D'}, related_name='doctor')
    patient = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'user_type': 'P'})
    date =  models.DateField()
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    reason = models.TextField()
    status = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['patient', 'doctor', 'date'], name='unique_booking')
        ]

    def __str__(self):
        return f"{self.doctor.get_full_name()}'s appointment with {self.patient.username}"

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine)
    # quantity = models.IntegerField() #? Dont know how to get quantity for each medicine
    instructions = models.TextField()

    def __str__(self):
        return f"{self.appointment.patient.username}'s prescription on {self.appointment.date}"
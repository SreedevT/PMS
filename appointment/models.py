from django.db import models
from accounts.models import User
from hospital.models import Medicine

class Appointment(models.Model):
    doctor = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'user_type': 'D'}, related_name='doctor')
    patient = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'user_type': 'P'})
    date =  models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor.get_full_name()}'s appointment with {self.patient.username}"

class Priscription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine)
    # quantity = models.IntegerField() #? Dont know how to get quantity for each medicine
    instructions = models.TextField()

    def __str__(self):
        return f"{self.appointment.patient.username}'s prescription on {self.appointment.date}"
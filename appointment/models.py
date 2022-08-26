import os
from django.db import models, connection
from accounts.models import User
from hospital.models import Medicine

#* More info on upload_to function: https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.FileField.upload_to
#* Rename uploaded report file: https://stackoverflow.com/questions/15140942/django-imagefield-change-file-name-on-upload
def path_and_rename(upload_to, field_name):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        
        department = instance.appointment.doctor.docprofile.department.name
    #     '''
    #             SELECT DISTINCT
    #                 hospital_department.name
    #             FROM appointment_appointment
    #             JOIN profiles_doctorprofile
    #             ON profiles_doctorprofile.user_id = %s
    #             JOIN hospital_department
    #             ON hospital_department.id = profiles_doctorprofile.department_id
    # ''', [app_id]
        print(connection.queries)
        filename = f'{instance.appointment.patient.username}_{instance.appointment.date}_{department}_{field_name}.{ext}'
        return os.path.join(upload_to, filename)
    return wrapper

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
        ordering = ['date', 'start_time']

    def __str__(self):
        return f"{self.doctor.get_full_name()}'s appointment with {self.patient.username} on {self.date}"


class Report(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='report')
    test_report = models.FileField(null=True, blank=True, upload_to=path_and_rename('files/report', 'report'))
    xray = models.FileField(null=True, blank=True, upload_to=path_and_rename('files/xray', 'xray'))
    ct = models.FileField(null=True, blank=True, upload_to=path_and_rename('files/ct', 'ct'))
    diagnosis = models.TextField()

    def __str__(self):
        return f"{self.appointment.patient.username}'s report on {self.appointment.date}"


class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine) #* More on m2m relationship: https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/, 
    #* https://docs.djangoproject.com/en/4.0/topics/db/models/#relationships-many-to-many
    #* https://dzone.com/articles/how-to-handle-a-many-to-many-relationship-in-datab

    # quantity = models.IntegerField() #? Dont know how to get quantity for each medicine
    #* Info on quanity: https://docs.djangoproject.com/en/4.0/topics/db/models/#extra-fields-on-many-to-many-relationships
    instructions = models.TextField()

    def __str__(self):
        return f"{self.appointment.patient.username}'s prescription on {self.appointment.date}"
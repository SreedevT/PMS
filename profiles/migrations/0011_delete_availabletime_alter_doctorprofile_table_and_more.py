# Generated by Django 4.1 on 2022-08-26 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_availabletime'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AvailableTime',
        ),
        migrations.AlterModelTable(
            name='doctorprofile',
            table='doctor_profile',
        ),
        migrations.AlterModelTable(
            name='patientprofile',
            table='patient_profile',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-30 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('D', 'Doctor'), ('P', 'Patient')], default='P', max_length=1),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-17 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_doctor_offered_patients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='offered_patients',
        ),
    ]
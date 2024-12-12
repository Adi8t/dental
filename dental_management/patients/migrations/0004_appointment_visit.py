# Generated by Django 5.1.1 on 2024-09-20 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
        ('doctors', '0008_alter_doctor_affiliated_clinics'),
        ('patients', '0003_remove_patient_next_appointment_procedure_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='doctors.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='patients.patient')),
                ('procedures', models.ManyToManyField(blank=True, related_name='appointments', to='doctors.procedure')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='clinics.clinic')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='doctors.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='patients.patient')),
                ('procedures_done', models.ManyToManyField(blank=True, related_name='visits', to='doctors.procedure')),
            ],
        ),
    ]
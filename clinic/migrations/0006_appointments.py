# Generated by Django 4.0.4 on 2022-05-10 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_alter_slot_avalible_slot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('panding', 'Pending'), ('completed', 'Completed'), ('absent', 'Absent'), ('canceled', 'Canceled')], default='panding', max_length=20)),
                ('description', models.TextField(default=None)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.slot')),
            ],
        ),
    ]

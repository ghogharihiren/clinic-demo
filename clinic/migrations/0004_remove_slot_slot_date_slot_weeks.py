# Generated by Django 4.0.4 on 2022-05-10 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_remove_slot_weeks_slot_slot_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='slot_date',
        ),
        migrations.AddField(
            model_name='slot',
            name='weeks',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuseday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]

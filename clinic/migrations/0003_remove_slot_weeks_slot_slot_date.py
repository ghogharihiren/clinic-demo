# Generated by Django 4.0.4 on 2022-05-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_remove_slot_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='weeks',
        ),
        migrations.AddField(
            model_name='slot',
            name='slot_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

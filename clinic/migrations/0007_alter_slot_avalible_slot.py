# Generated by Django 4.0.4 on 2022-05-11 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_appointments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='avalible_slot',
            field=models.IntegerField(),
        ),
    ]

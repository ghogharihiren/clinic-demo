# Generated by Django 4.0.4 on 2022-05-13 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0023_alter_user_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pic',
        ),
    ]

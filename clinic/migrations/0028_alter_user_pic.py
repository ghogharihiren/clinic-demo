# Generated by Django 4.0.4 on 2022-05-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0027_alter_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.FileField(upload_to='profile'),
        ),
    ]
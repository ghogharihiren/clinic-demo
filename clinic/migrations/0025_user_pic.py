# Generated by Django 4.0.4 on 2022-05-13 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0024_remove_user_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.FileField(default=1, upload_to='profile/'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0010_alter_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.ImageField(default='1.png', upload_to='profile'),
        ),
    ]

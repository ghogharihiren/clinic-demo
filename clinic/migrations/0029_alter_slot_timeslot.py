# Generated by Django 4.0.4 on 2022-05-13 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0028_alter_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='timeslot',
            field=models.CharField(choices=[('09:00 am To 10:00 am', '09:00 am To 10:00 am'), ('10:00 am To 11:00 am', '10:00 am TO 11:00 am'), ('11:00 am To 12:00 pm', '11:00 am To 12:00 pm'), ('12:00 pm To 01:00 pm', '12:00 pm To 01:00 pm'), ('02:00 pm To 03:00 pm', '02:00 pm To 03:00 pm'), ('03:00 pm To 04:00 pm', '03:00 pm To 04:00 pm'), ('04:00 pm To 05:00 pm', '04:00 pm To 05:00 pm')], max_length=50),
        ),
    ]
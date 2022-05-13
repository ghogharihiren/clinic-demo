
from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Type=(('mbbs','Mbbs'),('md','Md'),('ms','Ms'),('bhms','Bhms'),('bams','Bams'),('bpt','Bpt'))
    gender= (('male','Male'), ('female','Female'))
    Role=(('doctor','Doctor'),('patient','Patient'))
    addres=models.TextField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=10,choices=gender,null=True,blank=True)
    mobile=models.CharField(max_length=20)
    clinicname=models.CharField(max_length=50,null=True,blank=True)
    role=models.CharField(max_length=10,choices=Role,null=True,blank=True)
    types=models.CharField(max_length=10,choices=Type,null=True,blank=True)
    specialty=models.CharField(max_length=50,null=True,blank=True)
    pic=models.FileField(upload_to='profile')

    def __str__(self):
        return self.email
    
class Slot(models.Model):
    TIMESLOT = (
        ('09:00 am To 10:00 am', '09:00 am To 10:00 am'),
        ('10:00 am To 11:00 am', '10:00 am TO 11:00 am'),
        ('11:00 am To 12:00 pm', '11:00 am To 12:00 pm'),
        ('12:00 pm To 01:00 pm', '12:00 pm To 01:00 pm'),
        ('02:00 pm To 03:00 pm', '02:00 pm To 03:00 pm'),
        ('03:00 pm To 04:00 pm', '03:00 pm To 04:00 pm'),
        ('04:00 pm To 05:00 pm', '04:00 pm To 05:00 pm'),
    )
    WEEKS = (
        ('monday','Monday'),
        ('tuesday','Tuesday'),
        ('wednesday','Wednesday'),
        ('thursday','Thursday'),
        ('friday','Friday'),
        ('saturday','Saturday'),
    )
    doctor=models.ForeignKey(User,on_delete=models.CASCADE)
    weeks=models.CharField(max_length=10,choices=WEEKS)
    timeslot=models.CharField(max_length=50,choices=TIMESLOT)
    avalible_slot=models.IntegerField()
    
    def __str__(self):
        return self.doctor.username 
    
    
class Appointments(models.Model):
    STATUS = (
        ('pending','Pending'),
        ('completed','Completed'),
        ('absent','Absent'),
        ('canceled','Canceled'),
    ) 
    slot=models.ForeignKey(Slot,on_delete=models.CASCADE)
    patient=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=STATUS,default='pending')
    description= models.TextField(default=None)
    
    def __str__(self):
        return self.patient.email

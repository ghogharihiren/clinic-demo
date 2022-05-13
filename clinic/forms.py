
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import*
from django.contrib.auth import get_user_model
#User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','role']
        
        
class Userlogin(AuthenticationForm):
    username=forms.CharField(label='Username')
    password=forms.CharField(label='Password',widget=forms.PasswordInput())       
    
class Editprofile(forms.ModelForm):
    class Meta:
        model=User
        fields= ['username','email','role']     
 
 
class DoctorProfile(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','gender','types','clinicname','specialty','addres','pic','mobile'] 
        
class PatientProfile(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','gender','pic','mobile']           
        
class SlotForm(forms.ModelForm):
    class Meta:
        model=Slot
        fields=['weeks','timeslot','avalible_slot'] 
        
class EditSlot(forms.ModelForm):
    class Meta:
        model=Slot
        fields=['weeks','timeslot','avalible_slot']                 
        
class AppointmentBook(forms.ModelForm):
    class Meta:
        model=Appointments
        fields=['description']  
        
class EditAppointment(forms.ModelForm):
    class Meta:
        model=Appointments
        fields='__all__'     
        
    
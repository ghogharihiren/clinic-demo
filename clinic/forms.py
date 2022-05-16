
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import*
from django.contrib.auth import get_user_model
#User = get_user_model()

class RegisterForm(UserCreationForm):
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),
    )
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','role']
        widgets = {
            'role': forms.Select(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
             
               
        }
        
class Userlogin(AuthenticationForm):
    username=forms.CharField(label='Username')
    password=forms.CharField(label='Password',widget=forms.PasswordInput())   
    
class Editprofile(forms.ModelForm):
    class Meta:
        model=User
        fields= ['username','email','role']  
        
        
        widgets = {
            'role': forms.Select(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),             
        }
           
 
 
class DoctorProfile(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','gender','types','clinicname','specialty','addres','pic','mobile'] 
        
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'types': forms.Select(attrs={'class':'form-control'}),
            'clinicname': forms.TextInput(attrs={'class':'form-control'}),
            'specialty': forms.TextInput(attrs={'class':'form-control'}),
            'specialty': forms.TextInput(attrs={'class':'form-control'}),
            'addres':forms.Textarea(attrs={'class':'form-control'}),
            'clinicname': forms.TextInput(attrs={'class':'form-control'}),
            'pic': forms.FileInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),   
               
        }
class PatientProfile(forms.ModelForm):
    
   #gender = forms.CharField(widget=forms.choices(attrs={'class': 'myfieldclass'}))
    
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','gender','pic','mobile']     
              
        widgets = {
            'gender': forms.Select(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'pic': forms.FileInput(attrs={'class':'form-control'}),   
               
        }
        
class SlotForm(forms.ModelForm):
    class Meta:
        model=Slot
        fields=['weeks','timeslot','avalible_slot'] 
        
        widgets = {
            'weeks': forms.Select(attrs={'class':'form-control'}),
            'timeslot': forms.Select(attrs={'class':'form-control'}),
            'avalible_slot': forms.NumberInput(attrs={'class':'form-control'}),
        }
        
class EditSlot(forms.ModelForm):
    class Meta:
        model=Slot
        fields=['weeks','timeslot','avalible_slot'] 
        
        widgets = {
            'weeks': forms.Select(attrs={'class':'form-control'}),
            'timeslot': forms.Select(attrs={'class':'form-control'}),
            'avalible_slot': forms.NumberInput(attrs={'class':'form-control'}),
        }
        
        
                        
        
class AppointmentBook(forms.ModelForm):
    class Meta:
        model=Appointments
        fields=['description']  
        
        widget={
            'description': forms.Textarea(attrs={'class':'form-control'}),  
        }
        
class EditAppointment(forms.ModelForm):
    class Meta:
        model=Appointments
        fields='__all__'   
        widgets = {
        'status': forms.Select(attrs={'class':'form-control'}),
        'slot': forms.Select(attrs={'class':'form-control'}),
        'patient': forms.Select(attrs={'class':'form-control'}),
        'description': forms.TextInput(attrs={'class':'form-control'}),        
        }  
        
    
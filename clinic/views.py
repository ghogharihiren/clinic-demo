from django.shortcuts import redirect, render
from .forms import*
from .models import*
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordChangeForm
import random
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')


def forgot_password(request):
    password1=PasswordChangeForm(user=request.user)
    if request.method == "POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'your password change')
            logout(request)
            return redirect('login')
        else:
            messages.info(request,'enter correct password')
            return render(request,'forgot-password.html',{'pass':password1})
    else:
         return render(request,'forgot-password.html',{'pass':password1})
     
#---------------------------login/logout--------------------------------------------------

def loginpage(request):
    form1=Userlogin()
    if request.method == "POST":
        form=Userlogin(request=request,data=request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                if user.role == 'doctor':
                    return redirect('doctor-index')
                elif user.role =='patient':
                    return redirect('patient-index')
                else:
                    return redirect('admin-index')
            else:
                messages.info(request,'Enter correct username or password')
                return render(request,'login.html',{'form':form1})
        else:
            messages.info(request,'Enter correct username or password')
            return render(request,'login.html',{'form':form1})    
    return render(request,'login.html',{'form':form1}) 


def user_logout(request):
    logout(request)
    return redirect('login')

 
#-------------------------------Admin----------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def admin_index(request):
    user=User.objects.all()
    app=Appointments.objects.all()
    return render(request,'admin/admin-index.html',{'user':user,'app':app})

@login_required(login_url='/login/')
def patient_user(request):
    user=User.objects.filter(role='patient')[::-1]
    return render(request,'admin/patient-user.html',{'user':user})


@login_required(login_url='/login/')   
def doctor_user(request):
    user=User.objects.filter(role='doctor')[::-1]
    return render(request,'admin/doctor-user.html',{'user':user})


@login_required(login_url='/login/')
def profile(request,pk):
    pro=User.objects.get(id=pk)
    form=Editprofile(instance=pro)
    if request.method == "POST":
        fm=Editprofile(request.POST,instance=pro)
        if fm.is_valid():
            fm.save()
            if request.user.role == 'doctor':
                messages.success(request,'Profile update')
                return redirect('doctor-user')
            else:
                messages.success(request,'Profile update')
                return redirect('patient-user')
        else:
            messages.info(request,'enter the valid data')
            return render(request,'admin/profile.html',{'pro':pro,'form':form})
    return render(request,'admin/profile.html',{'pro':pro,'form':form})


@login_required(login_url='/login/')
def create_user(request):
    fm=RegisterForm()
    if request.method == 'POST':
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            message = f"""Hello your username is {form.cleaned_data['username']},
            and Your password is {form.cleaned_data['password1']}"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'],]
            send_mail( "your login details", message, email_from, recipient_list ) 
            form.save()
            return redirect('admin-index')
        messages.info(request,'Enter the valid data')
        return render(request,'admin/create-user.html',{"fm":fm})
    return render(request,'admin/create-user.html',{'fm':fm})


@login_required(login_url='/login/')
def delete_profile(request,pk):
    user=User.objects.get(id=pk)
    if user.role == 'doctor':
        user.delete()
        messages.success(request,'delete doctor successfully')
        return redirect('doctor-user')    
    else:
        user.delete()
        messages.success(request,'delete patient successfully')
        return redirect('patient-user')
    
@login_required(login_url='/login/')
def edit_appointment(request,pk):
    app=Appointments.objects.get(id=pk)    
    fm=EditAppointment(instance=app)
    if request.method == 'POST':
        form=EditAppointment(request.POST,instance=app)
        if form.is_valid():
            form.save()
            messages.success(request,'Appointment update')
            return redirect('admin-index')
        messages.info(request,'Enter the valid data')
        return render(request,'admin/edit-appointment.html',{'app':app,'fm':fm})
    return render(request,'admin/edit-appointment.html',{'app':app,'fm':fm})

@login_required(login_url='/login/')
def delete_appointment(request,pk):
    app=Appointments.objects.get(id=pk)
    app.delete()
    messages.success(request,'Appointment delete successfully')
    return redirect('admin-index')


#-----------------------------doctor-----------------------------------------------------------------------------------------


@login_required(login_url='/login/')
def doctor_index(request):
    slot=Slot.objects.filter(doctor=request.user)
    return render(request,'doctor/doctor-index.html',{"slot":slot})



@login_required(login_url='/login/')
def doctor_profile(request):

    form=DoctorProfile(instance=request.user)
    if request.method == "POST":
        form=DoctorProfile(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile update')
            return redirect('doctor-index')
        else:
            messages.info(request,'Enter the valid data')
            return render(request,'doctor/doctor-profile.html',{'fm':form})
    return render(request,'doctor/doctor-profile.html',{'fm':form})

@login_required(login_url='/login/')
def addslot(request):
    form1=SlotForm()
    if request.method == "POST":
        form=SlotForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.doctor=request.user
            f.save()
            messages.success(request,'add slot successfully')
            return redirect("doctor-index")
        else:
            messages.info(request,'Enter the valid data')
            return render(request,'doctor/addslot.html',{'form':form1})
    return render(request,'doctor/addslot.html',{'form':form1})   


@login_required(login_url='/login/')
def edit_slot(request,pk):
    slot=Slot.objects.get(id=pk)
    form=EditSlot(instance=slot)
    if request.method == 'POST':
        fm=EditSlot(request.POST,instance=slot)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Your slot update')
            return redirect('doctor-index')
        else:
            messages.info(request,'Enter the valid data')
            return render(request,'doctor/edit-slot.html',{'form':form})
    return render(request,'doctor/edit-slot.html',{'form':form})
        
@login_required(login_url='/login/')
def delete_slot(request,pk):
    slot=Slot.objects.get(id=pk)
    slot.delete()
    messages.success(request,'Your slot delete successfully')
    return redirect('doctor-index')
@login_required(login_url='/login/')
def appointment(request):
    app=Appointments.objects.all()
    return render(request,'doctor/appointment.html',{'app':app})
#-------------------------------patient--------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def patient_index(request):
    return render(request,'patient/patient-index.html')

@login_required(login_url='/login/')
def patient_profile(request):
    form=PatientProfile(instance=request.user)
    if request.method == 'POST':
        fm=PatientProfile(request.POST,request.FILES,instance=request.user)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Profile update') 
            return redirect('patient-index')
        messages.info(request,'Enter the valid data')
        return render(request,'patient/patient-profile.html',{'form':form})
            
    return render(request,'patient/patient-profile.html',{'form':form})   
            
            
@login_required(login_url='/login/')     
def doctor_details(request):
    user=User.objects.filter(role='doctor')
    return render(request,'patient/doctor-details.html',{'user':user})

@login_required(login_url='/login/')
def view_doctor(request,pk):
    user1=User.objects.get(id=pk)
    slot=Slot.objects.filter(doctor=user1)
    return render(request,'patient/view-doctor.html',{'slot':slot,'user1':user1})
    
@login_required(login_url='/login/')   
def view_appointment(request,pk):
    slot=Slot.objects.get(id=pk)
    form1=AppointmentBook()
    if request.method == 'POST':
        form=AppointmentBook(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.patient=request.user
            f.slot=slot
            f.save()
            slot.avalible_slot -= 1
            slot.save()
            messages.success(request,'your appointment booked')
            return redirect('patient-index')
        messages.info(request,'enter the valid data')
        return render(request,'patient/view-appoinment.html',{'slot':slot,'form':form1})
    return render(request,'patient/view-appoinment.html',{'slot':slot,'form':form1})
 
@login_required(login_url='/login/')       
def my_appointment(request):
    app=Appointments.objects.filter(patient=request.user)
    return render(request,'patient/my-appointment.html',{'app':app})    

@login_required(login_url='/login/')
def search_doctor(request):
    if request.method =="GET":
        search=request.GET.get('search')
        if search:
            user=User.objects.filter(first_name__icontains=search)
            slot=Slot.objects.filter(weeks__icontains=search)
            return render(request,'patient/search-doctor.html',{'user':user,'slot':slot})
        else:
            return redirect('patient-index')
    else:
        return redirect('patient-index')    
     

#----------------------------Appointment Status------------------------------------------------
@login_required(login_url='/login/')
def cancel_appointment(request,pk):
    app=Appointments.objects.get(id=pk)
    app.status='canceled'
    app.save()
    slot=Slot.objects.get(id=app.slot.id)
    slot.avalible_slot += 1
    slot.save()
    if request.user.role == 'doctor':
        messages.success(request,'Your appointment canceled')
        return redirect('appointment')
    else:
        messages.success(request,'Your appointment canceled')
        return redirect('my-appointment')

@login_required(login_url='/login/')
def complate_appointment(request,pk):
    app=Appointments.objects.get(id=pk)
    app.status ='completed' 
    app.save()  
    return redirect('appointment')

@login_required(login_url='/login/')
def absent(request,pk):
    app=Appointments.objects.get(id=pk)
    app.status='absent'
    app.save()
    return redirect('appointment')
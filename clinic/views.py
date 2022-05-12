
from urllib import request
from django.shortcuts import redirect, render
from .forms import*
from .models import*
from django.contrib.auth import authenticate,login,logout

def index(request):
    return render(request,'header.html')
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
                return render(request,'login.html',{'form':form1})
        else:
            return render(request,'login.html',{'form':form1})    
    return render(request,'login.html',{'form':form1}) 


def user_logout(request):
    logout(request)
    return redirect('login')

 
#-------------------------------Admin----------------------------------------------------------------------------------------
def admin_index(request):
    if request.user.is_authenticated:
        user=User.objects.all()
        app=Appointments.objects.all()
        return render(request,'admin/admin-index.html',{'user':user,'app':app})
    return redirect('login')

def patient_user(request):
    if request.user.is_authenticated:
       user=User.objects.filter(role='patient')[::-1]
       return render(request,'admin/patient-user.html',{'user':user})
    return redirect('login')

    
def doctor_user(request):
    if request.user.is_authenticated:
       user=User.objects.filter(role='doctor')[::-1]
       return render(request,'admin/doctor-user.html',{'user':user})
    return redirect('login')

    
def profile(request,pk):
    if request.user.is_authenticated:
        pro=User.objects.get(id=pk)
        if request.method == "POST":
            fm=Editprofile(request.POST,instance=pro)
            if fm.is_valid():
                fm.save()
                if request.user.role == 'doctor':
                    return redirect('doctor-user')
                else:
                    return redirect('patient-user')
            else:
                return render(request,'admin/profile.html',{'pro':pro})
        return render(request,'admin/profile.html',{'pro':pro})
    return redirect('login')


def create_user(request):
    if request.user.is_authenticated:
        fm=RegisterForm()
        if request.method == 'POST':
            form=RegisterForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin-index')
            return render(request,'admin/create-user.html',{"fm":fm})
        return render(request,'admin/create-user.html',{'fm':fm})
    return redirect(login)

def delete_profile(request,pk):
    user=User.objects.get(id=pk)
    if user.role == 'doctor':
        user.delete()
        return redirect('doctor-user')    
    else:
        user.delete()
        return redirect('patient-user')
    
    
def edit_appointment(request,pk):
    app=Appointments.objects.get(id=pk)    
    fm=EditAppointment(instance=app)
    if request.method == 'POST':
        form=EditAppointment(request.POST,instance=app)
        if form.is_valid():
            form.save()
            return redirect('admin-index')
        print(form.errors)
    return render(request,'admin/edit-appointment.html',{'app':app,'fm':fm})

def delete_appointment(request,pk):
    app=Appointments.objects.get(id=pk)
    app.delete()
    return redirect('admin-index')


#-----------------------------doctor-----------------------------------------------------------------------------------------
def doctor_index(request):
    if request.user.is_authenticated:
        slot=Slot.objects.filter(doctor=request.user)
        return render(request,'doctor/doctor-index.html',{"slot":slot})
    return redirect('login')

def doctor_profile(request):
    if request.user.is_authenticated:
        form=DoctorProfile(instance=request.user)
        if request.method == "POST":
            form=DoctorProfile(request.POST,request.FILES,instance=request.user)
            if form.is_valid():
                print("ouijhohuioo",form.cleaned_data['pic'])
                form.save()
                return redirect('doctor-index')
            else:
                return render(request,'doctor/doctor-profile.html',{'fm':form})
        return render(request,'doctor/doctor-profile.html',{'fm':form})
    else:
        return redirect('login')

def addslot(request):
    form1=SlotForm()
    if request.user.is_authenticated:
        if request.method == "POST":
            form=SlotForm(request.POST)
            if form.is_valid():
                f=form.save(commit=False)
                f.doctor=request.user
                f.save()
                return redirect("doctor-index")
            print(form.errors)
            return render(request,'doctor/addslot.html',{'form':form1})
        return render(request,'doctor/addslot.html',{'form':form1})   
    return redirect('login') 


def edit_slot(request,pk):
    slot=Slot.objects.get(id=pk)
    form=EditSlot(instance=slot)
    if request.method == 'POST':
        fm=EditSlot(request.POST,instance=slot)
        if fm.is_valid():
            fm.save()
            return redirect('doctor-index')
        else:
            return render(request,'doctor/edit-slot.html',{'form':form})
    return render(request,'doctor/edit-slot.html',{'form':form})
        

def delete_slot(request,pk):
    slot=Slot.objects.get(id=pk)
    slot.delete()
    return redirect('doctor-index')

def appointment(request):
    app=Appointments.objects.all()
    return render(request,'doctor/appointment.html',{'app':app})
#-------------------------------patient--------------------------------------------------------------------------------------
def patient_index(request):
    if request.user.is_authenticated:
       return render(request,'patient/patient-index.html')
    return redirect('login')


def patient_profile(request):
    if request.user.is_authenticated:
        form=PatientProfile(instance=request.user)
        if request.method == "POST":
            form=PatientProfile(request.POST,request.FILES,instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('patient-index')
            else:
                print(form.errors)
                return render(request,'patient/patient-profile.html')
        return render(request,'patient/patient-profile.html',{'form':form})
    else:
        return redirect('login')
    
    
def doctor_details(request):
    user=User.objects.filter(role='doctor')
    return render(request,'patient/doctor-details.html',{'user':user})

def view_doctor(request,pk):
    user1=User.objects.get(id=pk)
    slot=Slot.objects.filter(doctor=user1)
    return render(request,'patient/view-doctor.html',{'slot':slot,'user1':user1})
    
    
def view_appointment(request,pk):
    slot=Slot.objects.get(id=pk)
    if request.method == 'POST':
        form=AppointmentBook(request.POST)
        if form.is_valid():
            print(form)
            f=form.save(commit=False)
            f.patient=request.user
            f.slot=slot
            f.save()
            slot.avalible_slot -= 1
            slot.save()
            return redirect('patient-index')
        return render(request,'patient/view-appoinment.html',{'slot':slot})
    return render(request,'patient/view-appoinment.html',{'slot':slot})
        
def my_appointment(request):
    app=Appointments.objects.filter(patient=request.user)
    return render(request,'patient/my-appointment.html',{'app':app})    


def search_doctor(request):
    if request.method =="GET":
        search=request.GET.get('search')
        if search:
            user=User.objects.filter(first_name__icontains=search)
            return render(request,'patient/search-doctor.html',{'user':user})
        
    

#----------------------------Appointment Status------------------------------------------------
def cancel_appointment(request,pk):
    app=Appointments.objects.get(id=pk)
    app.status='canceled'
    app.save()
    slot=Slot.objects.get(id=app.slot.id)
    slot.avalible_slot += 1
    slot.save()
    if request.user.role == 'doctor':
        return redirect('appointment')
    else:
        return redirect('my-appointment')

def complate_appointment(request,pk):
    app=Appointments.objects.get(id=pk)
    app.status ='completed' 
    app.save()  
    return redirect('appointment')

def absent(request,pk):
    app=Appointments.objects.get(id=pk)
    app.status='absent'
    app.save()
    return redirect('appointment')
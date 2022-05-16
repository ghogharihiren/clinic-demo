from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
path('',views.index,name='index'),   
path('login/',views.loginpage,name='login'),
path('logout/',views.user_logout,name='logout'),
path('forgot-password/',views.forgot_password,name='forgot-password'),

    
#---------------------------------admin-------------------------------
path('admin-index/',views.admin_index,name='admin-index'),
path('patient-user/',views.patient_user,name='patient-user'),
path('doctor-user/',views.doctor_user,name='doctor-user'),
path('profile/<int:pk>',views.profile,name='profile'),    
path('delete/<int:pk>',views.delete_profile,name='delete'),
path('create-user/',views.create_user,name='create-user'),
path('delete-appointment/<int:pk>',views.delete_appointment,name='delete-appointment'),
path('edit-appointment/<int:pk>',views.edit_appointment,name='edit-appointment'),

#---------------------------------doctor------------------------------
path('doctor-index/',views.doctor_index,name='doctor-index'),
path('doctor-profile/',views.doctor_profile,name='doctor-profile'),
path('addslot/',views.addslot,name='addslot'),
path('delete-slot/<int:pk>',views.delete_slot,name='delete-slot'),
path('edit-slot/<int:pk>',views.edit_slot,name='edit-slot'),
path('appointment/',views.appointment,name='appointment'),
path('complate-appointment/<int:pk>',views.complate_appointment,name='complate-appointment'),
path('absent/<int:pk>',views.absent,name='absent'),

#---------------------------------patient-----------------------------    
path('patient-index/',views.patient_index,name='patient-index'),  
path('doctor-details/',views.doctor_details,name='doctor-details'),
path('view-doctor/<int:pk>',views.view_doctor,name='view-doctor'),
path('view-appoinment/<int:pk>',views.view_appointment,name='view-appointment'),
path('patient-profile/',views.patient_profile,name='patient-profile'),
path('my-appointment/',views.my_appointment,name='my-appointment'),
path('cancel-appointment/<int:pk>',views.cancel_appointment,name='cancel-appointment'),
path('search-doctor/',views.search_doctor,name='search-doctor'),
    
    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
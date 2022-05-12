from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User)
admin.site.register(Slot)
admin.site.register(Appointments)

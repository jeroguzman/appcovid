from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterDoctorForm
from .models import User, Doctor

# Register your models here.
# @admin.register(User)
# class EmployeeAdmin(UserAdmin):
#     fprm = UserRegisterDoctorForm
#     model = Doctor
#     ordering = ['correo']


admin.site.register(User)
admin.site.register(Doctor)
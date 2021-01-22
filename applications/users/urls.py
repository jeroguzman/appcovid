from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('register/paciente/', views.UserRegisterPacienteView.as_view(), name='user-register-paciente'),
    path('register/doctor/', views.UserRegisterDoctorView.as_view(), name='user-register-doctor'),
    path('accounts/login/', views.UserLoginView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('update-password/', views.UserUpdatePasswordView.as_view(), name='user-update-password'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('update-profile/<pk>', views.UserUpdateProfileView.as_view(), name='user-update-profile'),
]
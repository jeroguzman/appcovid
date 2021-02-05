from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('register/', views.UserRegisterPacienteView.as_view(), name='user-register-paciente'),
    path('accounts/login/', views.UserLoginView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('update-password/', views.UserUpdatePasswordView.as_view(), name='user-update-password'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('update-profile/<pk>', views.UserUpdateProfileView.as_view(), name='user-update-profile'),
    path('dashboard/profile/', views.UserDoctorProfileView.as_view(), name='user-doctor-profile'),
    path('dashboard/update-profile/<pk>', views.UserUpdateDoctorProfileView.as_view(), name='user-update-doctor-profile'),
    path('dashboard/update-firma/<pk>', views.UserUpdateDoctorFirmaView.as_view(), name='user-update-firma'),
]
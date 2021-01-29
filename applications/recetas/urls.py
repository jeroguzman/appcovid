from django.urls import path
from . import views

app_name = 'recetas_app'

urlpatterns = [
    path('recetas/', views.RecetasPacienteView.as_view(), name='recetas-paciente'),
    path('dashboard/recetas/', views.RecetasDoctorView.as_view(), name='recetas-doctor'),
    # path('dashboard/recetas/sent', views.SentMailDoctor.as_view(), name='recetas-sent-doctor'),
]
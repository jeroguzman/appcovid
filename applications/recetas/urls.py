from django.urls import path
from . import views

app_name = 'recetas_app'

urlpatterns = [
    path('recetas/', views.RecetasView.as_view(), name='recetas'),
]
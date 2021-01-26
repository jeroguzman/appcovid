from django.db import models
from applications.users.models import Paciente, Doctor

# Create your models here.
class Receta(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    contenido = models.TextField()

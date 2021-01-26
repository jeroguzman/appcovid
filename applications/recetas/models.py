from django.db import models
from django.conf import settings
from applications.users.models import Paciente

# Create your models here.
class Receta(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    contenido = models.TextField()

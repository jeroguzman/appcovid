from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
class User(models.Model):

    SEXO = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]

    nombre = models.CharField(max_length=120)
    aPaterno = models.CharField(max_length=120, null=True)
    aMaterno = models.CharField(max_length=120, null=True)
    edad = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    direccion = models.CharField(max_length=500, null=True)
    cp = models.PositiveIntegerField(validators=[RegexValidator('r^\d{5}$')], null=True)
    telefono = models.PositiveIntegerField(null=True)
    correo = models.EmailField(null=True)
    contrasena = models.CharField(max_length=120, null=True)
    contrasena2 = models.CharField(max_length=120, null=True)
    avisoPrivacidad = models.BooleanField(null=False, default=False)


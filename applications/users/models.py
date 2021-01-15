from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    #nombre, apellido paterno, apellido materno, edad, sexo, direccion, cp, telefono, correo, contrasena, confirmar contrasena, aviso de privacidad

    SEXO = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]

    nombre = models.CharField(max_length=120)
    aPaterno = models.CharField(max_length=120, null=True, blank=True)
    aMaterno = models.CharField(max_length=120, null=True, blank=True)
    edad = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(110)], null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True, blank=True)
    direccion = models.CharField(max_length=500, null=True, blank=True)
    cp = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.PositiveIntegerField(null=True, unique=True)
    correo = models.EmailField(null=True, unique=True)
    avisoPrivacidad = models.BooleanField(null=False, default=False, blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'telefono'

    REQUIRED_FIELDS = ['correo']

    objects = UserManager()

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.aPaterno, self.aMaterno)

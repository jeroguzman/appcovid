from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self, telefono, correo, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            telefono=telefono,
            correo=correo,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, telefono, correo, password=None, **extra_fields):
        return self._create_user(telefono, correo, password, False, False, **extra_fields)
    
    def create_superuser(self, telefono, correo, password=None, **extra_fields):
        return self._create_user(telefono, correo, password, True, True, **extra_fields)


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from persona.models import Persona


class UsuarioManager(BaseUserManager):
    def create_user(self, username, numero_documento, password=None):
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        if not numero_documento:
            raise ValueError('El usuario debe tener un número de documento')

        user = self.model(
            username=username,
            numero_documento=numero_documento,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, numero_documento, password=None):
        user = self.create_user(
            username=username,
            password=password,
            numero_documento=numero_documento,
        )
        user.rol = 'admin'
        user.status = 'activo'
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    ROL_CHOICES = [
        ('regente', 'Regente'),
        ('admin', 'Admin'),
    ]
    
    STATUS_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    rol = models.CharField(max_length=10, choices=ROL_CHOICES)
    numero_documento = models.OneToOneField(Persona, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='activo')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['numero_documento']

    objects = UsuarioManager()

    def __str__(self):
        return self.username

from django.db import models

class Persona(models.Model):
    TIPOS_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
    ]

    nombre_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    tipo_documento = models.CharField(max_length=2, choices=TIPOS_DOCUMENTO)
    numero_documento = models.CharField(max_length=20, primary_key=True)
    numero_telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nombre_completo

from django.db import models

class Producto(models.Model):
    
    nombre_producto = models.CharField(max_length=255)
    codigo_invima = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre_producto} ({self.codigo_invima})'
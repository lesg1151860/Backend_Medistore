from django.db import models

class Producto(models.Model):
    PRESENTACION_OPCIONES = [
        ('Tableta', 'Tableta'),
        ('Capsula', 'Capsula'),
        ('Jarabe', 'Jarabe'),
        ('Suspension', 'Suspension'),
        ('Inyectable', 'Inyectable'),
        ('Pomada', 'Pomada'),
        ('Crema', 'Crema'),
        ('Gota', 'Gota'),
        ('Aerosol o inhaladores', 'Aerosol'),
        ('Inhalador', 'Inhalador'),
        ('Supositorio', 'Supositorio'),
        ('Polvo', 'Polvo')
    ]

    id = models.AutoField(primary_key=True)
    registro_invima = models.CharField(max_length=16, unique=True, default='Desconocido')
    nombre = models.CharField(max_length=50, default='Nombre por definir')
    marca = models.CharField(max_length=30, default='Sin marca')
    presentacion = models.CharField(max_length=25, choices=PRESENTACION_OPCIONES, default='Tableta')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.nombre} - {self.marca}"
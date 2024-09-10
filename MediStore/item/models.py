from django.db import models

class Item(models.Model):
    ESTADO_OPCIONES = [
        ('disponible', 'Disponible'),
        ('vendido', 'Vendido'),
        ('danado', 'Dañado'),
        ('vencido', 'Vencido'),
    ]

    codigo_barras = models.CharField(max_length=50, primary_key=True)
    producto_id = models.ForeignKey('producto.Producto', on_delete=models.CASCADE)
    codigo_lote = models.ForeignKey('lote.Lote', on_delete=models.CASCADE, to_field='codigo')
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='disponible')

    def __str__(self):
        return f'{self.codigo_barras} - {self.producto_id.nombre} - {self.estado}'

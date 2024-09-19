from django.db import models

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    factura_id = models.ForeignKey('factura.Factura', on_delete=models.CASCADE)
    item_cod_barras = models.ForeignKey('item.Item', on_delete=models.CASCADE, to_field='codigo_barras')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id} - Factura {self.factura_id.id}"

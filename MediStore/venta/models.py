from django.db import models
from .models import Factura
from .models import Lote     

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    factura_id = models.ForeignKey(Factura, on_delete=models.CASCADE)
    item_codigo_barras = models.ForeignKey(Lote, on_delete=models.CASCADE, to_field='codigo_barras')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id} - Factura {self.factura_id.id}"

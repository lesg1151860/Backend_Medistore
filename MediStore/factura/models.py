from django.db import models
from django.utils import timezone
from django.conf import settings

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=timezone.now)
    regente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id} - Total: {self.total_pagar}"

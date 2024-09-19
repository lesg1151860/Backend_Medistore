from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Lote(models.Model):
    codigo_barras = models.CharField(primary_key=True, max_length=50)
    fecha_ingreso = models.DateField(default=timezone.now)
    fecha_vencimiento = models.DateField()

    def clean(self):
        if self.fecha_vencimiento and self.fecha_ingreso:
            if self.fecha_vencimiento < self.fecha_ingreso:
                raise ValidationError('La fecha de vencimiento no puede ser anterior a la fecha de ingreso')

    def save(self, *args, **kwargs):
        self.clean()
        super(Lote, self).save(*args, **kwargs)

    def __str__(self):
        return self.codigo_barras

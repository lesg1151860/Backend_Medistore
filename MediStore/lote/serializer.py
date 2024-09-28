from rest_framework import serializers
from .models import Lote
from django.utils import timezone

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ['codigo_barras', 'fecha_ingreso', 'fecha_vencimiento']

    def validate_fecha_vencimiento(self, value):
        
        if value < timezone.now().date():
            raise serializers.ValidationError("La fecha de vencimiento no puede ser anterior a la fecha actual.")
        return value

from rest_framework import serializers
from .models import Factura

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id', 'fecha', 'regente', 'total_pagar']
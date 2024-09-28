from rest_framework import serializers
from .models import Factura
from usuario.serializer import UsuarioSerializer  # Adjust the import path as necessary

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id', 'fecha', 'regente', 'total_pagar']

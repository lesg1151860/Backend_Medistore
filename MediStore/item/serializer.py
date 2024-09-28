from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
    
    def validate_codigo_barras(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("El código de barras debe contener únicamente caracteres numéricos.")
        return value
        
    def create(self, validated_data):
        return Item.objects.create(**validated_data)

class ItemEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['estado']

    def validate_estado(self, value):
        if value not in dict(Item.ESTADO_OPCIONES).keys():
            raise serializers.ValidationError("El estado seleccionado no es válido.")
        return value

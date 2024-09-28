from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre_completo', 'email', 'tipo_documento', 'numero_documento', 'numero_telefono']
        
class PersonaUpDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre_completo', 'email', 'tipo_documento', 'numero_documento', 'numero_telefono']

    def update(self, instance, validated_data):
        instance.nombre_completo = validated_data.get('nombre_completo', instance.nombre_completo)
        instance.email = validated_data.get('email', instance.email)
        instance.tipo_documento = validated_data.get('tipo_documento', instance.tipo_documento)
        instance.numero_documento = validated_data.get('numero_documento', instance.numero_documento)
        instance.numero_telefono = validated_data.get('numero_telefono', instance.numero_telefono)
        instance.save()
        return instance

    
class PersonaDeleteSerializer(serializers.Serializer):
    numero_documento = serializers.CharField()

    def validate_numero_documento(self, value):
        try:
            persona = Persona.objects.get(numero_documento=value)
        except Persona.DoesNotExist:
            raise serializers.ValidationError("Persona no encontrada")
        return value

    def delete(self, validated_data):
        persona = Persona.objects.get(numero_documento=validated_data['numero_documento'])
        persona.delete()
        return persona
from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre_completo', 'email', 'tipo_documento', 'numero_documento', 'numero_telefono']
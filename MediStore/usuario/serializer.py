from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'rol', 'numero_documento', 'status']
        extra_kwargs = {
            'password': {'write_only': True}  # Evitar que el campo password se exponga en las respuestas GET
        }

class CreateUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'rol', 'numero_documento', 'status']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Este método encripta la contraseña antes de guardarla
    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            rol=validated_data['rol'],
            numero_documento=validated_data['numero_documento'],
            status=validated_data['status']
        )
        user.set_password(validated_data['password'])  # Encripta la contraseña
        user.save()
        return user
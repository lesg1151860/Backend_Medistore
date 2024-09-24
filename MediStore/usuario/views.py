from rest_framework import generics
from .models import Usuario
from .serializer import UsuarioSerializer

# Vista para listar todos los usuarios
class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vista para crear un nuevo usuario
class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
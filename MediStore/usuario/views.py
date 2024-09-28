from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializer import CreateUsuarioSerializer, UsuarioSerializer, UsuarioUpdateSerializer

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = CreateUsuarioSerializer
    
class UsuarioUpdateView(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioUpdateSerializer
    lookup_field = 'username'
    
class UsuarioDeleteView(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    lookup_field = 'username'

    def destroy(self, request, *args, **kwargs):
        username = self.kwargs['username']
        if request.user.username == username:
            return Response({"error": "No puedes eliminar tu propio usuario."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
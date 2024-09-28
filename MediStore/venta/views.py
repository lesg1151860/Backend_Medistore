from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from venta.models import Venta
from .serializer import VentaSerializer
from rest_framework.generics import DestroyAPIView

class VentaListView(APIView):
    def get(self, request):
        ventas = Venta.objects.all()
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VentaCreateView(APIView):
    def post(self, request):
        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VentaDeleteView(DestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()  # Obtiene la instancia a eliminar
            self.perform_destroy(instance)  # Elimina la instancia
            return Response(status=status.HTTP_204_NO_CONTENT)  # Respuesta 204 si se elimina exitosamente
        except Venta.DoesNotExist:
            return Response({"error": "Venta no encontrada."}, status=status.HTTP_404_NOT_FOUND)  # Respuesta 404 si no se encuentra
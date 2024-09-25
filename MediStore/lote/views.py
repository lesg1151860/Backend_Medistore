from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from .models import Lote
from .serializer import LoteSerializer
from rest_framework.response import Response

class LoteListView(generics.ListAPIView):
    queryset = Lote.objects.all()  # Obtenemos todos los lotes de la base de datos
    serializer_class = LoteSerializer

class LoteCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Guardar el nuevo Lote
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoteDeleteView(APIView):
    def delete(self, request, codigo_barras, *args, **kwargs):
        try:
            lote = Lote.objects.get(codigo_barras=codigo_barras)
            lote.delete()
            return Response({"detail": "Lote eliminado con éxito."}, status=status.HTTP_204_NO_CONTENT)
        except Lote.DoesNotExist:
            return Response({"detail": "Lote no encontrado."}, status=status.HTTP_404_NOT_FOUND)
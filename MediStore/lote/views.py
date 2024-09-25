from rest_framework import generics
from .models import Lote
from .serializer import LoteSerializer

class LoteListView(generics.ListAPIView):
    queryset = Lote.objects.all()  # Obtenemos todos los lotes de la base de datos
    serializer_class = LoteSerializer

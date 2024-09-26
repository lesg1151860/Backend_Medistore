from rest_framework import generics
from .models import Item
from .serializer import ItemEstadoSerializer, ItemSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemEstadoUpdateView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemEstadoSerializer
    lookup_field = 'codigo_barras'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    lookup_field = 'codigo_barras'
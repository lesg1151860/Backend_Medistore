from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import Factura
from .serializer import FacturaSerializer

class FacturaListView(ListAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FacturaCreateView(CreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)

class FacturaDetailView(RetrieveAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FacturaDeleteView(DestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Factura.DoesNotExist:
            return Response({"error": "Factura no encontrada."}, status=status.HTTP_404_NOT_FOUND)
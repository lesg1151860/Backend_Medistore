from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Persona
from .serializer import PersonaDeleteSerializer, PersonaSerializer, PersonaUpDateSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import NotFound

class PersonaListView(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [OrderingFilter]
    ordening_fields = ["numero_documento"]

class PersonaCreateView(APIView):
    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonaSearchView(APIView):
    def get(self, request, numero_documento=None):
        try:
            persona = Persona.objects.get(numero_documento=numero_documento)
            serializer = PersonaSerializer(persona)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response({'Error': 'Persona no encontrada'}, status=status.HTTP_404_NOT_FOUND)

class PersonaUpdateView(APIView):
    
    def get_object(self, numero_documento):
        try:
            return Persona.objects.get(numero_documento=numero_documento)
        except Persona.DoesNotExist:
            raise NotFound(detail="Persona no encontrada dentro del sistema.")

    def put(self, request, numero_documento):
        persona = self.get_object(numero_documento)
        serializer = PersonaUpDateSerializer(persona, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonaDeleteView(APIView):

    def delete(self, request, numero_documento):
        try:
            persona = Persona.objects.get(numero_documento=numero_documento)
        except Persona.DoesNotExist:
            raise NotFound(detail="Persona no encontrada.")
        
        persona.delete()
        return Response({"message": "Persona eliminada correctamente."}, status=status.HTTP_204_NO_CONTENT)
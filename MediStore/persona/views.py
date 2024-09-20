from rest_framework import generics
from .models import Persona
from .serializer import PersonaSerializer

class PersonaListCreateView(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

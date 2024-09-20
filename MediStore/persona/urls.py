from django.urls import path
from .views import PersonaListCreateView

urlpatterns = [
    path('api/personas/', PersonaListCreateView.as_view(), name='personas-list-create'),
]


from django.urls import path
from .views import UsuarioCreateView, UsuarioListView

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuer-list'),  # URL para listar los usuarios
    path('usuarios/create/', UsuarioCreateView.as_view(), name='usuario-create'),  # Para la vista basada en clases
]

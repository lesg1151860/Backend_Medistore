from django.urls import path
from .views import UsuarioCreateView, UsuarioDeleteView, UsuarioListView, UsuarioUpdateView

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuer-list'),
    path('usuarios/create/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuarios/update/<str:username>/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuarios/delete/<str:username>/', UsuarioDeleteView.as_view(), name='usuario-delete'),
]

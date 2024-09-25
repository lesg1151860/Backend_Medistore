from django.urls import path
from .views import LoteCreateView, LoteDeleteView, LoteListView

urlpatterns = [
    path('lotes/', LoteListView.as_view(), name='lote-list'),
    path('lotes/create/', LoteCreateView.as_view(), name='lote-create'),
    path('lotes/delete/<str:codigo_barras>/', LoteDeleteView.as_view(), name='eliminar-lote'),
]

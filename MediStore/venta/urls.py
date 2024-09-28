from django.urls import path
from .views import VentaCreateView, VentaDeleteView, VentaListView

urlpatterns = [
    path('ventas/', VentaListView.as_view(), name='venta-list'),
    path('ventas/create/', VentaCreateView.as_view(), name='venta-create'),
    path('ventas/delete/<int:pk>/', VentaDeleteView.as_view(), name='venta-delete'),
]

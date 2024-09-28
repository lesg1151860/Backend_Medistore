from django.urls import path
from .views import FacturaCreateView, FacturaDeleteView, FacturaListView, FacturaDetailView

urlpatterns = [
    path('facturas/', FacturaListView.as_view(), name='factura-list'),
    path('facturas/create/', FacturaCreateView.as_view(), name='factura-create'),
    path('facturas/<int:pk>/', FacturaDetailView.as_view(), name='factura-detail'),
    path('facturas/delete/<int:pk>/', FacturaDeleteView.as_view(), name='factura-delete'),
]
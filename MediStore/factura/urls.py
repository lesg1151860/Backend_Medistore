from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacturaCreateView, FacturaViewSet

router = DefaultRouter()
router.register(r'facturas', FacturaViewSet)

urlpatterns = [
    path('facturas/', include(router.urls)),
    path('facturas/create/', FacturaCreateView.as_view(), name='factura-create'),
]

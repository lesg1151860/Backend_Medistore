from django.urls import path
from .views import ProductoList, ProductoDetail

urlpatterns = [
    path('productos/', ProductoList.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
]

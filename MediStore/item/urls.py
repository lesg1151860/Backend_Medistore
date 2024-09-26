from django.urls import path
from .views import ItemEstadoUpdateView, ItemListCreateView  

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list'),
    path('items/update-status/<str:codigo_barras>/', ItemEstadoUpdateView.as_view(), name='item-estado-update'),
]

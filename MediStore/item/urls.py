from django.urls import path
from .views import ItemDeleteView, ItemEstadoUpdateView, ItemListCreateView  

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list'),
    path('items/update-status/<str:codigo_barras>/', ItemEstadoUpdateView.as_view(), name='item-estado-update'),
    path('items/delete/<str:codigo_barras>/', ItemDeleteView.as_view(), name='item-delete'),
]

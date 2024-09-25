from django.urls import path
from .views import LoteListView

urlpatterns = [
    path('lotes/', LoteListView.as_view(), name='lote-list'),
]

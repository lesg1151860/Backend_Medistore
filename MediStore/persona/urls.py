from django.urls import  path
from .views import PersonaCreateView, PersonaDeleteView, PersonaListView, PersonaSearchView, PersonaUpdateView

urlpatterns = [
    path('personas/', PersonaListView.as_view(), name='persona-list'),
    path('personas/create/', PersonaCreateView.as_view(), name='persona-create'),
    path('personas/search/<str:numero_documento>/', PersonaSearchView.as_view(), name='persona-search'),
    path('personas/update/<str:numero_documento>/', PersonaUpdateView.as_view(), name='persona-update'),
    path('personas/delete/<str:numero_documento>/', PersonaDeleteView.as_view(), name='persona-delete'),
]
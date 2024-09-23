from django.urls import  path
from .views import PersonaCreateView, PersonaDeleteView, PersonaListView, PersonaSearchView, PersonaUpDateView

urlpatterns = [
    path('personas/', PersonaListView.as_view(), name='persona-list'),
    path('personas/create/', PersonaCreateView.as_view(), name='persona-create'),
    path('personas/search/<str:numero_documento>/', PersonaSearchView.as_view(), name='persona-search'),
    path('personas/update/<str:nombre_completo>/', PersonaUpDateView.as_view(), name='persona-update'),
    path('personas/delete/<str:numero_documento>/', PersonaDeleteView.as_view(), name='persona-delete'),
]
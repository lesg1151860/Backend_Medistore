"""
URL configuration for MediStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from django.views.generic.base import RedirectView
# from django.contrib.staticfiles.storage import staticfiles_storage
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('persona.urls')),
    path('', include('usuario.urls')),
    path('', include('lote.urls')),
    path('', include('producto.urls')),
    path('', include('item.urls')),
    path('', include('factura.urls')),
    # path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('src/favicon.ico')))
]

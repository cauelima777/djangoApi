"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include 
from rest_framework import routers
from categoria.views import categoriaView
from cliente.views import clienteView
from exercicio.views import exercicioView
from treino.views import treinoView

rotas = routers.DefaultRouter()
rotas.register(r'categoria',categoriaView, basename='categoria'),
rotas.register(r'cliente',clienteView, basename='cliente'),
rotas.register(r'exercicio',exercicioView, basename='exercicio'),
rotas.register(r'treino',treinoView, basename='exercicio'),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(rotas.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

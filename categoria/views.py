from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria 
from .serializers import categoriaSerializer
from rest_framework import permissions
# Create your views here.

class categoriaView(viewsets.ModelViewSet): 

    queryset = Categoria.objects.all()
    serializer_class = categoriaSerializer
    permission_classes = [permissions.IsAuthenticated]
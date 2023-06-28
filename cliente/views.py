
from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import clienteSerializer
from rest_framework import permissions
# Create your views here.

class clienteView(viewsets.ModelViewSet): 

    queryset = Cliente.objects.all()
    serializer_class = clienteSerializer
    permission_classes = [permissions.IsAuthenticated]
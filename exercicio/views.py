from django.shortcuts import render
from rest_framework import viewsets
from .models import Exercicio
from .serializers import exercicioSerializer
from rest_framework import permissions
# Create your views here.

class exercicioView(viewsets.ModelViewSet): 

    queryset = Exercicio.objects.all()
    serializer_class = exercicioSerializer
    permission_classes = [permissions.IsAuthenticated]
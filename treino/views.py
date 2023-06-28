from django.shortcuts import render
from rest_framework import viewsets
from .models import Treino
from .serializers import treinoSerializer
from rest_framework import permissions
# Create your views here.

class treinoView(viewsets.ModelViewSet): 

    queryset = Treino.objects.all()
    serializer_class = treinoSerializer
    permission_classes = [permissions.IsAuthenticated]
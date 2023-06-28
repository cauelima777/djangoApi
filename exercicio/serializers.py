from rest_framework import serializers 
from .models import Exercicio

class exercicioSerializer(serializers.ModelSerializer): 

    class Meta: 

        model = Exercicio

        fields = '__all__' 
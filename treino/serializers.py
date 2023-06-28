from rest_framework import serializers 
from .models import Treino

class treinoSerializer(serializers.ModelSerializer): 

    class Meta: 

        model = Treino

        fields = '__all__' 
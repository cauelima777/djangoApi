from rest_framework import serializers 
from .models import Categoria

class categoriaSerializer(serializers.ModelSerializer): 

    class Meta: 

        model = Categoria 

        fields = '__all__' 
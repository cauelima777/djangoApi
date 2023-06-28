from django.db import models
from categoria.models import Categoria


# Create your models here.
class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
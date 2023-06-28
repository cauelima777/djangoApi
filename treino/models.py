from django.db import models
from cliente.models import Cliente
from exercicio.models import Exercicio

class Treino(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    data = models.DateField()
    series = models.PositiveIntegerField()
    repeticoes = models.PositiveIntegerField()
    carga = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.cliente.nome} - {self.exercicio.nome}"
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    objetivo = models.TextField()

    def __str__(self):
        return self.nome
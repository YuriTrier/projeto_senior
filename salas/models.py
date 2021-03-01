from django.db import models

class Salas(models.Model):
    nome = models.CharField(max_length=100)
    lotacao = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nome + " - " + str(self.lotacao)

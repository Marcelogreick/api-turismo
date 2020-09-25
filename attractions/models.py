from django.db import models

class Attractions(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    funcionamento = models.TextField()
    idade_minima = models.IntegerField()

    def __srt__(self):
        return self.nome
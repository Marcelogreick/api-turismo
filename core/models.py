from django.db import models
from attractions.models import Attractions
from comment.models import Comment
from assessments.models import Assessments
from adresses.models import Adresses

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions)
    comment = models.ManyToManyField(Comment)
    assessments = models.ManyToManyField(Assessments)
    adresses = models.ForeignKey(Adresses, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
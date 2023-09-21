from django.db import models
from analyse.models import Analyse

class Mesure(models.Model):
    temps_de_comptage = models.DateTimeField()
    aire_nette = models.FloatField()
    incertitude_aire_nette = models.FloatField()
    taux_de_comptage = models.FloatField()
    incertitude_taux_de_comptage = models.FloatField()

    class Meta:
        abstract = True


class BruitDeFond(Mesure):
    analyse = models.ForeignKey(Analyse, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bruit de fond : {self.pk}"

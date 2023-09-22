from django.db import models
from models.mesure import Mesure


class Etalon(Mesure):
    nom = models.CharField(max_length=15)
    famille = models.CharField(max_length=15)
    masse = models.FloatField(blank=True, null=True)
    activite = models.FloatField(blank=True, null=True)
    incertitude_activite = models.FloatField(blank=True, null=True)
    facteur_de_conversion = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.famille}"

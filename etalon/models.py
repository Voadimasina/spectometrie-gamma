from django.db import models
from models.mesure import Mesure


class Etalon(Mesure):
    nom = models.CharField(max_length=10)
    famille = models.CharField(max_length=10)
    masse = models.FloatField()
    activite = models.FloatField()
    incertitude_activite = models.FloatField()
    facteur_de_conversion = models.FloatField()

    def __str__(self):
        return f"{self.nom} {self.famille}"

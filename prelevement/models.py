from django.db import models
from produit.models import Produit

class Mesure(models.Model):
    temps_de_comptage = models.DateTimeField()
    aire_nette = models.FloatField()
    incertitude_aire_nette = models.FloatField()
    taux_de_comptage = models.FloatField()
    incertitude_taux_de_comptage = models.FloatField()

    class Meta:
        abstract = True


class Prelevement(Mesure):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f"prelevement numero :{self.pk}"

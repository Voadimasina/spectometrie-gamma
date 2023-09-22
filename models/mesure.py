from django.db import models

class Mesure(models.Model):
    temps_de_comptage = models.FloatField()
    aire_nette = models.FloatField()
    incertitude_aire_nette = models.FloatField()
    taux_de_comptage = models.FloatField(null=True, blank=True)
    incertitude_taux_de_comptage = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True
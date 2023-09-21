from django.db import models

class Mesure(models.Model):
    temps_de_comptage = models.DateTimeField()
    aire_nette = models.FloatField()
    incertitude_aire_nette = models.FloatField()
    taux_de_comptage = models.FloatField()
    incertitude_taux_de_comptage = models.FloatField()

    class Meta:
        abstract = True


class Etalon(Mesure):
    nom = models.CharField(max_length=10)
    famille = models.CharField(max_length=10)
    masse = models.FloatField()
    activite = models.FloatField()
    incertitude_activite = models.FloatField()
    facteur_de_conversion = models.FloatField()

    def __str__(self):
        return f"{self.nom} {self.famille}"
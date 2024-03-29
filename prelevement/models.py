from django.db import models
from produit.models import Produit
from models.mesure import Mesure

class Prelevement(Mesure):
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)
    masse = models.FloatField()

    def __str__(self):
        return f"prelevement numero :{self.pk}"

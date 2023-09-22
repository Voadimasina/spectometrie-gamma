from django.db import models
from analyse.models import Analyse
from models.mesure import Mesure

class BruitDeFond(Mesure):
    analyse = models.ForeignKey(Analyse, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bruit de fond : {self.pk}"

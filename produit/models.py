from django.db import models
from analyse.models import Analyse

class Produit(models.Model):
    analyse = models.ForeignKey(Analyse, on_delete=models.CASCADE)
    type_du_produit = models.CharField(max_length=30)
    description = models.TextField()
    quantite = models.FloatField()

    def __str__(self):
        return f"produit :{self.type_du_produit}"
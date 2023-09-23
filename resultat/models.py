from django.db import models
from etalon.models import Etalon
from prelevement.models import Prelevement
from bruit_de_fond.models import BruitDeFond
from produit.models import Produit
from math import sqrt

class Resultat(models.Model):
    etalon = models.ForeignKey(Etalon, on_delete=models.CASCADE)
    prelevement = models.ForeignKey(Prelevement, on_delete=models.CASCADE)
    bruit_de_fond = models.ForeignKey(BruitDeFond, on_delete=models.CASCADE)
    activite = models.FloatField(null=True, blank=True) # Aech
    incertitude_activite = models.FloatField(null=True, blank=True)#bAech
    teneur = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Receuil des donnees:
        masse_etalon = self.etalon.masse
        masse_echantillon = self.prelevement.masse
        activite_etalon = self.etalon.activite
        incertitude_activite_etalon = self.etalon.incertitude_activite
        facteur_convertion = self.etalon.facteur_de_conversion

        ##Aire nette:
        aire_nette_etalon = self.etalon.aire_nette

        aire_nette_prelevement = self.prelevement.aire_nette

        aire_nette_bf = self.bruit_de_fond.aire_nette

        incertitude_aire_nette_etalon = self.etalon.incertitude_aire_nette

        incertitude_aire_nette_prelevement = self.prelevement.incertitude_aire_nette

        incertitude_aire_bf = self.bruit_de_fond.incertitude_aire_nette

        ##Temps de comptage:

        temps_comptage_etalon = self.etalon.temps_de_comptage

        temps_comptage_prelevement = self.prelevement.temps_de_comptage

        temps_comptage_bf = self.bruit_de_fond.temps_de_comptage

        ###Valeure nette aire nette:
        aire_nette_Etalon = aire_nette_etalon - aire_nette_bf
        
        aire_nette_Prelevement = aire_nette_prelevement - aire_nette_bf

        incertitude_aire_nette_Etalon = sqrt((incertitude_aire_nette_etalon ** 2) + (incertitude_aire_bf ** 2))

        incertitude_aire_nette_Prelevement = sqrt((incertitude_aire_nette_prelevement ** 2) + (incertitude_aire_bf ** 2))
        
        incertitude_aire_nette_bf = self.bruit_de_fond.incertitude_aire_nette

        ####Calcul taux de comptage:
        taux_comptage_etalon = aire_nette_Etalon / temps_comptage_etalon

        taux_comptage_prelevement = aire_nette_Prelevement / temps_comptage_prelevement

        taux_comptage_bf = aire_nette_bf / temps_comptage_bf

        incertitude_taux_comptage_Etalon = incertitude_aire_nette_Etalon / temps_comptage_etalon

        incertitude_taux_comptage_Prelevement = incertitude_aire_nette_Prelevement / temps_comptage_prelevement
        
        incertitude_taux_comptage_bf = incertitude_aire_nette_bf / temps_comptage_bf

        ###Valeure nette taux de comptage:
        taux_comptage_Etalon = taux_comptage_etalon - taux_comptage_bf
        
        taux_comptage_Prelevement = taux_comptage_prelevement - taux_comptage_bf

        incertitude_taux_comptage_Et = sqrt((incertitude_taux_comptage_Etalon ** 2) + (incertitude_taux_comptage_bf ** 2))
        
        incertitude_taux_comptage_Pr = sqrt((incertitude_taux_comptage_Prelevement ** 2) + incertitude_taux_comptage_bf)
        
        # Calcul de l'activité:
        activite_echantillon = (activite_etalon * taux_comptage_Prelevement * masse_etalon) / (taux_comptage_Etalon * masse_echantillon)
        
        # Calcul de l'incertitude de l'activité
        incertitude_activite = activite_echantillon * sqrt(((incertitude_taux_comptage_Et / taux_comptage_Etalon)**2) + ((incertitude_taux_comptage_Pr / taux_comptage_Prelevement)**2) + ((incertitude_activite_etalon / activite_etalon)**2))

        #Calcul teneur:
        teneur = activite_echantillon / facteur_convertion

        self.activite = activite_echantillon
        self.incertitude_activite = incertitude_activite
        self.teneur = teneur
        super(Resultat, self).save(*args, **kwargs)

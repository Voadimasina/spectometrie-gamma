from django.db import models

class Responsable(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

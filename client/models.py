from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nom

from django.db import models
from client.models import Client

class Analyse(models.Model):
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Analyse du {self.date}"

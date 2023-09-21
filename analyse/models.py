from django.db import models

class Analyse(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"Analyse du {self.date}"

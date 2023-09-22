from django import forms
from .models import BruitDeFond

class BruitDeFondForm(forms.ModelForm):
    class Meta:
        model = BruitDeFond
        fields = [
            'temps_de_comptage',
            'aire_nette',
            'incertitude_aire_nette',
            'taux_de_comptage',
            'incertitude_taux_de_comptage',
            'analyse',
        ]

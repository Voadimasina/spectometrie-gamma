from django import forms
from .models import Prelevement

class PrelevementForm(forms.ModelForm):
    class Meta:
        model = Prelevement
        fields = [
            'temps_de_comptage',
            'aire_nette',
            'incertitude_aire_nette',
            'taux_de_comptage',
            'incertitude_taux_de_comptage',
            'produit'
        ]

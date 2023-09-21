from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = [
            'analyse',
            'type_du_produit',
            'description',
            'quantite'
        ]

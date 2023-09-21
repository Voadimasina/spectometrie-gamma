from django import forms
from .models import Etalon

class EtalonForm(forms.ModelForm):
    class Meta:
        model = Etalon
        fields = ['nom', 'masse', 'activite', 'incertitude_activite', 'facteur_de_conversion']

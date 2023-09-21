from django import forms
from .models import Analyse

class AnalyseForm(forms.ModelForm):
    class Meta:
        model = Analyse
        fields = ['date']

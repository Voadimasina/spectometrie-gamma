from django import forms
from .models import Responsable

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = '__all__'

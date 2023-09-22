from rest_framework import serializers
from .models import BruitDeFond

class BruitDeFondSerializer(serializers.ModelSerializer):
    class Meta:
        model = BruitDeFond
        fields = '__all__'

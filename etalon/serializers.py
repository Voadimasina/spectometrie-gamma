from rest_framework import serializers
from .models import Etalon

class ÉtalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etalon
        fields = '__all__'

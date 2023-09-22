from rest_framework import serializers
from .models import Prelevement

class PrelevementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prelevement
        fields = '__all__'

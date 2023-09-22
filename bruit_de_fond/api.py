from rest_framework import generics
from .models import BruitDeFond
from .serializers import BruitDeFondSerializer

class BruitDeFondListCreateView(generics.ListCreateAPIView):
    queryset = BruitDeFond.objects.all()
    serializer_class = BruitDeFondSerializer

class BruitDeFondRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BruitDeFond.objects.all()
    serializer_class = BruitDeFondSerializer

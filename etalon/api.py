from rest_framework import generics
from .models import Etalon
from .serializers import EtalonSerializer

class EtalonListCreateView(generics.ListCreateAPIView):
    queryset = Etalon.objects.all()
    serializer_class = EtalonSerializer

class EtalonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etalon.objects.all()
    serializer_class = EtalonSerializer

from rest_framework import generics
from .models import Resultat
from .serializers import ResultatSerializer

class ResultatListCreateView(generics.ListCreateAPIView):
    queryset = Resultat.objects.all()
    serializer_class = ResultatSerializer

class ResultatRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resultat.objects.all()
    serializer_class = ResultatSerializer

from rest_framework import generics
from .models import Analyse
from .serializers import AnalyseSerializer

class AnalyseListCreateView(generics.ListCreateAPIView):
    queryset = Analyse.objects.all()
    serializer_class = AnalyseSerializer

class AnalyseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Analyse.objects.all()
    serializer_class = AnalyseSerializer

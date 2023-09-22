from rest_framework import generics
from .models import Prelevement
from .serializers import PrelevementSerializer

class PrelevementListCreateView(generics.ListCreateAPIView):
    queryset = Prelevement.objects.all()
    serializer_class = PrelevementSerializer

class PrelevementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prelevement.objects.all()
    serializer_class = PrelevementSerializer

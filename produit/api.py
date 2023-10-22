from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Produit
from .serializers import ProduitSerializer
from prelevement.models import Prelevement
from prelevement.serializers import PrelevementSerializer


class ProduitListCreateView(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ProduitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    
class ProduitPrelevementView(APIView):
    def get(self, request, pk):
        try:
            produit = Produit.objects.get(pk=pk)
        except Produit.DoesNotExist:
            return Response({"error": "Produit not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            prelevement = Prelevement.objects.get(produit=produit)
        except Prelevement.DoesNotExist:
            return Response({"error": "Prelevement not found for this Produit"}, status=status.HTTP_404_NOT_FOUND)

        serialized_prelevement = PrelevementSerializer(prelevement).data

        return Response({
            'produit_id': produit.id,
            'prelevement': serialized_prelevement
        }, status=status.HTTP_200_OK)
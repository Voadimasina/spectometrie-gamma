from rest_framework import generics, status
from rest_framework.response import Response
from .models import BruitDeFond
from .serializers import BruitDeFondSerializer

class BruitDeFondListCreateView(generics.ListCreateAPIView):
    queryset = BruitDeFond.objects.all()
    serializer_class = BruitDeFondSerializer

    def create(self, request, *args, **kwargs):
        # Obtenir les données du formulaire Bruit de fond
        data = request.data
        aire_nette = data.get('aire_nette')
        temps_de_comptage = data.get('temps_de_comptage')

        # Calculer le taux de comptage et son incertitude
        taux_de_comptage = aire_nette / temps_de_comptage
        incertitude_taux_de_comptage = data.get('incertitude_aire_nette') / temps_de_comptage

        # Ajouter les calculs aux données avant de les sérialiser
        data['taux_de_comptage'] = taux_de_comptage
        data['incertitude_taux_de_comptage'] = incertitude_taux_de_comptage

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BruitDeFondRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BruitDeFond.objects.all()
    serializer_class = BruitDeFondSerializer

    def perform_update(self, serializer):
        # Obtenir les données du formulaire Bruit de fond
        data = serializer.validated_data
        aire_nette = data.get('aire_nette')
        temps_de_comptage = data.get('temps_de_comptage')

        # Calculer le taux de comptage et son incertitude
        taux_de_comptage = aire_nette / temps_de_comptage
        incertitude_taux_de_comptage = data.get('incertitude_aire_nette') / temps_de_comptage

        # Mettre à jour les données avec les calculs
        serializer.save(taux_de_comptage=taux_de_comptage, incertitude_taux_de_comptage=incertitude_taux_de_comptage)

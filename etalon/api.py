from rest_framework import generics, status
from rest_framework.response import Response
from .models import Etalon
from .serializers import ÉtalonSerializer

class EtalonListCreateView(generics.ListCreateAPIView):
    queryset = Etalon.objects.all()
    serializer_class = ÉtalonSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        aire_nette = data.get('aire_nette')
        temps_de_comptage = data.get('temps_de_comptage')
        incertitude_aire_nette = data.get('incertitude_aire_nette')


        taux_de_comptage = aire_nette / temps_de_comptage
        incertitude_taux_de_comptage = incertitude_aire_nette / temps_de_comptage


        data['taux_de_comptage'] = taux_de_comptage
        data['incertitude_taux_de_comptage'] = incertitude_taux_de_comptage

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        # if 'aire_nette' in data and 'temps_de_comptage' in data:
        #     aire_nette = data['aire_nette']
        #     temps_de_comptage = data['temps_de_comptage']


        #     if aire_nette is not None and temps_de_comptage is not None and temps_de_comptage != 0:
        #         taux_de_comptage = aire_nette / temps_de_comptage
        #         data['taux_de_comptage'] = taux_de_comptage

        #         serializer = self.get_serializer(data=data)
        #         serializer.is_valid(raise_exception=True)
        #         serializer.save()

        #         headers = self.get_success_headers(serializer.data)
        #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        #     else:
        #         return Response({"error": "Les données nécessaires pour le calcul ne sont pas valides."}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     return Response({"error": "Les données nécessaires pour le calcul sont manquantes."}, status=status.HTTP_400_BAD_REQUEST)

class EtalonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etalon.objects.all()
    serializer_class = ÉtalonSerializer

    def perform_update(self, serializer):

        data = serializer.validated_data
        aire_nette = data.get('aire_nette')
        temps_de_comptage = data.get('temps_de_comptage')


        taux_de_comptage = aire_nette / temps_de_comptage
        incertitude_taux_de_comptage = data.get('incertitude_aire_nette') / temps_de_comptage

        serializer.save(taux_de_comptage=taux_de_comptage, incertitude_taux_de_comptage=incertitude_taux_de_comptage)
        # if 'aire_nette' in data and 'temps_de_comptage' in data:
        #     aire_nette = data['aire_nette']
        #     temps_de_comptage = data['temps_de_comptage']

        #     # Vérifiez si les valeurs nécessaires ne sont pas nulles
        #     if aire_nette is not None and temps_de_comptage is not None and temps_de_comptage != 0:
        #         taux_de_comptage = aire_nette / temps_de_comptage
        #         data['taux_de_comptage'] = taux_de_comptage

        #         serializer = self.get_serializer(data=data)
        #         serializer.is_valid(raise_exception=True)
        #         serializer.save()

        #         headers = self.get_success_headers(serializer.data)
        #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        #     else:
        #         return Response({"error": "Les données nécessaires pour le calcul ne sont pas valides."}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     return Response({"error": "Les données nécessaires pour le calcul sont manquantes."}, status=status.HTTP_400_BAD_REQUEST)

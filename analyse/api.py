from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Analyse
from .serializers import AnalyseSerializer
from produit.models import Produit
from produit.serializers import ProduitSerializer
from bruit_de_fond.models import BruitDeFond
from bruit_de_fond.serializers import BruitDeFondSerializer
from prelevement.serializers import PrelevementSerializer
from prelevement.models import Prelevement
from resultat.serializers import ResultatSerializer
from resultat.models import Resultat

class AnalyseListTotal(APIView):
    def get(self, request, pk, format=None):
        try:
            analyse = Analyse.objects.get(pk=pk)
        except Analyse.DoesNotExist:
            return Response({"detail": "Analyse not found"}, status=404)

        produits = []
        for produit in Produit.objects.filter(analyse=analyse):
            prelevement = Prelevement.objects.get(produit=produit)

            resultats = Resultat.objects.filter(prelevement=prelevement)

            resultat_data = []
            for resultat in resultats:
                resultat_data.append({
                    "id": resultat.id,
                    "type_du_produit": produit.type_du_produit,
                    "nom": resultat.etalon.nom,
                    "famille": resultat.etalon.famille,
                    "quantite": produit.quantite,
                    "activite": resultat.activite,
                    "incertitude_activite": resultat.incertitude_activite,
                    "teneur": resultat.teneur,
                })

            produits.append({
                "prelevement": prelevement.id,
                "resultats": resultat_data,
            })

        response_data = {
            "id": analyse.id,
            "produits": produits
        }

        return Response(response_data)

class AnalyseResultatsListTotal(APIView):
    def get(self, request, pk, format=None):
        try:
            analyse = Analyse.objects.get(pk=pk)
        except Analyse.DoesNotExist:
            return Response({"detail": "Analyse not found"}, status=status.HTTP_404_NOT_FOUND)

        produits = []

        for produit in Produit.objects.filter(analyse=analyse):
            try:
                prelevement = Prelevement.objects.get(produit=produit)
            except Prelevement.DoesNotExist:
                prelevement = None

            resultats = Resultat.objects.filter(prelevement=prelevement)

            resultat_data = []
            for resultat in resultats:
                resultat_data.append({
                    "id": resultat.id,
                    "activite": resultat.activite,
                    "incertitude_activite": resultat.incertitude_activite,
                    "teneur": resultat.teneur,
                })

            produits.append({
                "produit": {
                    "type_du_produit": produit.type_du_produit,
                    "description": produit.description,
                    "quantite": produit.quantite,
                },
                "prelevement": prelevement.id if prelevement else None,
                "resultats": resultat_data,
            })

        response_data = {
            "id": analyse.id,
            "produits": produits
        }

        return Response(response_data)


class AnalyseResultatsList(APIView):
    def get(self, request, pk, format=None):
        try:
            analyse = Analyse.objects.get(pk=pk)
        except Analyse.DoesNotExist:
            return Response({"detail": "Analyse not found"}, status=status.HTTP_404_NOT_FOUND)

        produits = []
        for produit in Produit.objects.filter(analyse=analyse):
            try:
                prelevement = Prelevement.objects.get(produit=produit)
            except Prelevement.DoesNotExist:
                prelevement = None

            resultats = Resultat.objects.filter(prelevement=prelevement)

            resultat_data = []
            for resultat in resultats:
                resultat_data.append({
                    "id": resultat.id,
                    "activite": resultat.activite,
                    "incertitude_activite": resultat.incertitude_activite,
                    "teneur": resultat.teneur,
                })

            produits.append({
                "produit": produit.id,
                "prelevement": prelevement.id if prelevement else None,
                "resultats": resultat_data,
            })

        response_data = {
            "id": analyse.id,
            "produits": produits
        }

        return Response(response_data)

class AnalyseDetails(APIView):
    def get(self, request, pk):
        try:
            analyse = Analyse.objects.get(pk=pk)
        except Analyse.DoesNotExist:
            return Response({"error": "Analyse not found"}, status=status.HTTP_404_NOT_FOUND)

        # Récupérer les informations sur les produits et prélevements
        produits = Produit.objects.filter(analyse=analyse)
        bruit_de_fond = BruitDeFond.objects.filter(analyse=analyse).first()  # Utiliser filter().first() pour obtenir None si non trouvé

        produit_data = []
        for produit in produits:
            # Récupérer le prélevement lié au produit s'il existe
            prelevement = Prelevement.objects.filter(produit=produit).first()

            produit_info = {
                "id": produit.id if produit else "",  # Si produit est None, id sera une chaîne vide
                "prelevement": prelevement.id if prelevement else "",  # Idem pour le prélevement
            }
            produit_data.append(produit_info)

        # Sérialiser les informations
        response_data = {
            "id": analyse.id,
            "produit": produit_data,
            "bruit_de_fond": bruit_de_fond.id if bruit_de_fond else "",  # Idem pour le bruit de fond
        }

        return Response(response_data, status=status.HTTP_200_OK)

    
class AnalyseListCreateView(generics.ListCreateAPIView):
    queryset = Analyse.objects.all()
    serializer_class = AnalyseSerializer

class AnalyseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Analyse.objects.all()
    serializer_class = AnalyseSerializer

class AnalyseListWithClientDetails(APIView):
    def get(self, request):
        # Récupérez toutes les analyses avec les détails du client
        analyses = Analyse.objects.all()
        serialized_analyses = []

        for analyse in analyses:
            serialized_analyse = AnalyseSerializer(analyse).data
            serialized_analyse['client'] = {
                'id': analyse.client.id,
                'nom': analyse.client.nom,
                'adresse': analyse.client.adresse
            }
            serialized_analyses.append(serialized_analyse)

        return Response(serialized_analyses, status=status.HTTP_200_OK)
    
class AnalyseProductCount(APIView):
    def get(self, request, pk):
        try:
            analyse = Analyse.objects.get(pk=pk)
        except Analyse.DoesNotExist:
            return Response({"error": "Analyse not found"}, status=status.HTTP_404_NOT_FOUND)

        products = Produit.objects.filter(analyse=analyse)
        serialized_products = ProduitSerializer(products, many=True).data

        return Response({
            'analyse_id': analyse.id,
            'product_count': len(products),
            'products': serialized_products
        }, status=status.HTTP_200_OK)
    
class AnalyseBruitDeFond(APIView):
    def get(self, request, pk):
        try:
            analyse = Analyse.objects.get(pk=pk)
        except Analyse.DoesNotExist:
            return Response({"error": "Analyse not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            bruit_de_fond = BruitDeFond.objects.get(analyse=analyse)
        except BruitDeFond.DoesNotExist:
            return Response({"error": "Bruit de fond not found for this Analyse"}, status=status.HTTP_404_NOT_FOUND)

        
        # try:
        #     analyse = Analyse.objects.get(pk=pk)
        # except Analyse.DoesNotExist:
        #     return 

        # try:
        #     bruit_de_fond = BruitDeFond.objects.get(analyse=analyse)
        # except BruitDeFond.DoesNotExist:
        #     return 

        serialized_bruit_de_fond = BruitDeFondSerializer(bruit_de_fond).data

        return Response({
            'analyse_id': analyse.id,
            'bruit_de_fond': serialized_bruit_de_fond
        }, status=status.HTTP_200_OK)

class AnalyseCreateWithClientDetails(APIView):
    def post(self, request):
        serializer = AnalyseSerializer(data=request.data)
        if serializer.is_valid():
            analyse = serializer.save()
            serialized_analyse = AnalyseSerializer(analyse).data
            serialized_analyse['client'] = {
                'id': analyse.client.id,
                'nom': analyse.client.nom,
                'adresse': analyse.client.adresse
            }
            return Response(serialized_analyse, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            analyse = Analyse.objects.get(pk=pk)
        except Analyse.DoesNotExist:
            return Response({"error": "Analyse not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AnalyseSerializer(analyse, data=request.data)
        if serializer.is_valid():
            analyse = serializer.save()
            serialized_analyse = AnalyseSerializer(analyse).data
            serialized_analyse['client'] = {
                'id': analyse.client.id,
                'nom': analyse.client.nom,
                'adresse': analyse.client.adresse
            }
            return Response(serialized_analyse, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

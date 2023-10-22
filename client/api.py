from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer
from rest_framework.pagination import PageNumberPagination

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        search_term = self.request.query_params.get('search', '')
        queryset = Client.objects.filter(nom__icontains=search_term)
        return queryset

class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientListAnalysisDetails(APIView):
    def get(self, request):
        
        clients = Client.objects.all()
        serialized_clients = []

        for client in clients:
            serialized_client = ClientSerializer(client).data
            serialized_client['analyse'] = [
                {'id': analyse.id, 'date': analyse.date}
                for analyse in client.analyse_set.all()
            ]
            serialized_clients.append(serialized_client)

        return Response(serialized_clients, status=status.HTTP_200_OK)
    
class ClientDetailAnalysisDetails(APIView):
    def get(self, request, pk):
        
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

        serialized_client = ClientSerializer(client).data
        serialized_client['analyse'] = [
            {'id': analyse.id, 'date': analyse.date}
            for analyse in client.analyse_set.all()
        ]

        return Response(serialized_client, status=status.HTTP_200_OK)
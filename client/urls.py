from django.urls import path
from .views import create_client, delete_client, detail_client, update_client, list_clients
from .api import ClientListCreateView, ClientRetrieveUpdateDestroyView, ClientDetailAnalysisDetails, ClientListAnalysisDetails

app_name = 'client'

urlpatterns = [
    path('', list_clients, name='list'),
    path('ajout/', create_client, name='create'),
    path('<int:client_id>/', detail_client, name='detail'),
    path('update/<int:client_id>/', update_client, name='update'),
    path('delete/<int:client_id>/', delete_client, name='delete'),
     path(
        'api',
        ClientListCreateView.as_view(),
        name='client-list-create'
    ),
    path(
        'api/<int:pk>',
        ClientRetrieveUpdateDestroyView.as_view(),
        name='client-retrieve-update-destroy'
    ),
    path(
        'api/with-analyses-details',
        ClientListAnalysisDetails.as_view(),
        name='client-list-analyse-details'
    ),
    path(
        'api/<int:pk>/analyse-details',
        ClientDetailAnalysisDetails.as_view(),
        name='client-detail-analyse-details'
    ),
]
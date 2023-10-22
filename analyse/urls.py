from django.urls import path
# from .views import create_analyse, list_analyses, delete_analyse, detail_analyse, update_analyse
from .api import AnalyseListCreateView, AnalyseRetrieveUpdateDestroyView, AnalyseListWithClientDetails, AnalyseProductCount, AnalyseBruitDeFond,AnalyseCreateWithClientDetails, AnalyseDetails, AnalyseResultatsList, AnalyseResultatsListTotal, AnalyseListTotal

app_name = 'analyse'

urlpatterns = [
    # path('', list_analyses, name='list_analyses'),
    # path('create/', create_analyse, name='create_analyse'),
    # path('<int:analyse_id>/', detail_analyse, name='detail_analyse'),
    # path('update/<int:analyse_id>/', update_analyse, name='update_analyse'),
    # path('delete/<int:analyse_id>/', delete_analyse, name='delete_analyse'),
    path(
        'api',
        AnalyseListCreateView.as_view(),
        name='analyse-list-create'
    ),
    path(
        'api/<int:pk>',
        AnalyseRetrieveUpdateDestroyView.as_view(),
        name='analyse-retrieve-update-destroy'
    ),
    path(
        'api/client-details',
        AnalyseListWithClientDetails.as_view(),
        name='analyse-client-details'
    ),
    path(
        'api/<int:pk>/produit',
        AnalyseProductCount.as_view(),
        name='analyse-product-count'
    ),
    path(
        'api/<int:pk>/bf',
        AnalyseBruitDeFond.as_view(),
        name='analyse-bruitdefond'
    ),
    path('api/ajout-clients', AnalyseCreateWithClientDetails.as_view(), name='analyse-create-with-client-details'
    ),
    path('api/<int:pk>/modifier-client', AnalyseCreateWithClientDetails.as_view(), name='analyse-update-with-client-details' ),
    path('api/<int:pk>/details', AnalyseDetails.as_view(), name='analyse-details'),
    path('api/<int:pk>/resultats', AnalyseResultatsList.as_view(), name='analyse-resultats-list'),
    path('api/<int:pk>/rs', AnalyseResultatsListTotal.as_view(), name='analyse-resultats-total'),
    path('api/<int:pk>/total', AnalyseListTotal.as_view(), name='analyse-resultats-list-total'),

]

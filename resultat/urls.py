from django.urls import path
from .api import ResultatListCreateView, ResultatRetrieveUpdateDestroyView

urlpatterns = [
    path(
        'api',
        ResultatListCreateView.as_view(),
        name='resultat-list-create'
        ),
    path(
        'api/<int:pk>',
        ResultatRetrieveUpdateDestroyView.as_view(),
        name='resultat-retrieve-update-destroy'
        ),
]

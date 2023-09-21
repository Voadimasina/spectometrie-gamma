from django.urls import path
from .views import create_produit, delete_produit, detail_produit, list_produits, update_produit
from .api import ProduitListCreateView, ProduitDetailView

app_name = 'produit'

urlpatterns = [
    path('', list_produits, name='list'),
    path('create/', create_produit, name='create'),
    path('<int:produit_id>/', detail_produit, name='detail'),
    path('update/<int:produit_id>/', update_produit, name='update'),
    path('delete/<int:produit_id>/', delete_produit, name='delete'),
    path(
        'api',
        ProduitListCreateView.as_view(),
        name='produit-list-create'
    ),
    path(
        'api/<int:pk>',
        ProduitDetailView.as_view(),
        name='produit-detail'
    ),
]

from django.urls import path
from .views import create_bruitdefond, list_bruitdefond, delete_bruitdefond, detail_bruitdefond, update_bruitdefond
from .api import BruitDeFondListCreateView, BruitDeFondRetrieveUpdateDestroyView

app_name = 'bruitdefond'

urlpatterns = [
    path('', list_bruitdefond, name='list'),
    path('create/', create_bruitdefond, name='create'),
    path('<int:bruitdefond_id>/', detail_bruitdefond, name='detail'),
    path('update/<int:bruitdefond_id>/', update_bruitdefond, name='update'),
    path('delete/<int:bruitdefond_id>/', delete_bruitdefond, name='delete'),
    path(
        'api',
        BruitDeFondListCreateView.as_view(),
        name='bruitdefond-list-create'
    ),
    path(
        'api/<int:pk>',
        BruitDeFondRetrieveUpdateDestroyView.as_view(),
        name='bruitdefond-retrieve-update-destroy'
    ),

]

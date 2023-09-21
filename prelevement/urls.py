from django.urls import path
from .views import create_prelevement, delete_prelevement, detail_prelevement, list_prelevements, update_prelevement

app_name = 'prelevement'

urlpatterns = [
    path('', list_prelevements, name='list'),
    path('create/', create_prelevement, name='create'),
    path('<int:prelevement_id>/', detail_prelevement, name='detail'),
    path('update/<int:prelevement_id>/', update_prelevement, name='update'),
    path('delete/<int:prelevement_id>/', delete_prelevement, name='delete'),
]

from django.urls import path
from .views import create_etalon, delete_etalon, detail_etalon, list_etalons, update_etalon

app_name = 'etalon'

urlpatterns = [
    path('', list_etalons, name='list'),
    path('create/', create_etalon, name='create'),
    path('<int:etalon_id>/', detail_etalon, name='detail'),
    path('update/<int:etalon_id>/', update_etalon, name='update'),
    path('delete/<int:etalon_id>/', delete_etalon, name='delete'),
]

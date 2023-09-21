from django.urls import path
from .views import list_responsables, create_responsable, delete_responsable, detail_responsable, update_responsable

app_name = 'responsable'

urlpatterns = [
    path('', list_responsables, name='list'),
    path('create/', create_responsable, name='create'),
    path('<int:responsable_id>/', detail_responsable, name='detail'),
    path('update/<int:responsable_id>/', update_responsable, name='update'),
    path('delete/<int:responsable_id>/', delete_responsable, name='delete'),
]

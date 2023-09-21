from django.urls import path
from .views import create_analyse, list_analyses, delete_analyse, detail_analyse, update_analyse
from .api import AnalyseListCreateView, AnalyseRetrieveUpdateDestroyView

app_name = 'analyse'

urlpatterns = [
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
    path('', list_analyses, name='list_analyses'),
    path('create/', create_analyse, name='create_analyse'),
    path('<int:analyse_id>/', detail_analyse, name='detail_analyse'),
    path('update/<int:analyse_id>/', update_analyse, name='update_analyse'),
    path('delete/<int:analyse_id>/', delete_analyse, name='delete_analyse'),
]

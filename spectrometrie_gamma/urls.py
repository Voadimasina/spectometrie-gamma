from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('responsable/', include('responsable.urls')),
    path('client/', include('client.urls')),
    path('analyse/', include('analyse.urls')),
    path('produit/', include('produit.urls')),
    path('prelevement/', include('prelevement.urls')),
    path('bruit_de_fond/', include('bruit_de_fond.urls')),
    path('etalon/', include('etalon.urls')),
    path('resultat/', include('resultat.urls')),
]

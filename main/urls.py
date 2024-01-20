# main/urls.py
from django.urls import path
from .views import homepage,destinacije_lista, smjestaji_lista, rezervacije_lista

urlpatterns = [
    path('', homepage, name='homepage'),
    path('destinacije/', destinacije_lista, name='destinacije-lista'),
    path('smjestaji/', smjestaji_lista, name='smjestaji-lista'),
    path('rezervacije/', rezervacije_lista, name='rezervacije-lista'),
]

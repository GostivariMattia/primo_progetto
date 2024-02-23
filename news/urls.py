from django.urls import path
from .views import *

app_name= 'news'

urlpatterns = [
    path('home/',home,name="home"),
    path('articoli/<int:pk>',articoloDetailView, name="articolo_detail"),
    path('giornalista/<int:pk>',giornalistaDetailView, name="giornalista_detail"),
    path('giornalista/lista/<int:pk>',listaArticoli, name="lista_articoli_giornalista"),
    path('giornalista/lista/',listaArticoli, name="lista_articoli"),
    path('lista/',query_base, name="query_base"),
    path('indexnews/',indexnews,name="indexnews"),
    path('giornalisti_list_api',giornalisti_list_api, name="giornalista_list_api"),
    path('giornalista_api/<int:pk>',giornalista_api,name="giornalista_api"),
    path('articoli_list_api',articoli_list_api,name="articoli_list_api"),
    path('articolo_api/<int:pk>',articolo_api,name="articolo_api")
]

from django.urls import path
from .views import home,articoloDetailView,listaArticoli,query_base

app_name= 'news'

urlpatterns = [
    path('',home,name="homeview"),
    path('articoli/<int:pk>',articoloDetailView, name="articolo_detail"),
    path('giornalista/lista/<int:pk>',listaArticoli, name="lista_articoli_giornalista"),
    path('giornalista/lista/',listaArticoli, name="lista_articoli"),
    path('lista/',query_base, name="query_base"),
    #path('query_base/',query_base,name=query_base),
]

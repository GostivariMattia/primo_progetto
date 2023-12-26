from django.urls import path
from .views import home,articoloDetailView,listaArticoli,query_base,giornalistaDetailView,indexnews

app_name= 'news'

urlpatterns = [
    path('home/',home,name="home"),
    path('articoli/<int:pk>',articoloDetailView, name="articolo_detail"),
    path('giornalista/<int:pk>',giornalistaDetailView, name="giornalista_detail"),
    path('giornalista/lista/<int:pk>',listaArticoli, name="lista_articoli_giornalista"),
    path('giornalista/lista/',listaArticoli, name="lista_articoli"),
    path('lista/',query_base, name="query_base"),
    path('indexnews/',indexnews,name="indexnews"),
    #path('query_base/',query_base,name=query_base),
]

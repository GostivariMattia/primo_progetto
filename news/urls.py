from django.urls import path
from .views import home,articoloDetailView,listaArticoli

app_name= 'news'

urlpatterns = [
    path('',home,name="homeview"),
    path('articoli/<int:pk>',articoloDetailView, name="articolo_detail"),
    path('giornalista/lista/<int:pk>',listaArticoli, name="lista_articoli_giornalista"),
    path('giornalista/lista/',listaArticoli, name="lista_articoli")
]

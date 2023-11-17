from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Articolo,Giornalista
# Create your views here.

"""
def home(request):
    a=""
    g=""
    for art in Articolo.objects.all():
        a+=(art.titolo+ "<br>")

    for gio in Giornalista.objects.all():
        g+=(gio.nome + "<br>")
    response="Articoli:<br>" + a + "<br>Giornalisti:<br>" +g
    
    return HttpResponse("<h1>" +response+"</h1>")    


def home(request):
    a=[]
    g=[]
    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome)

    response=str(a) +"<br>" +str(g)
    print(response)
    return HttpResponse("<h1>" +response+"</h1>")
"""
def home(request):
    articoli=Articolo.objects.all()
    giornalisti=Giornalista.objects.all()
    context={"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage_news.html",context)


def articoloDetailView(request,pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context  = {"articolo": articolo}
    return render(request, "articolo_detail.html",context)


def listaArticoli(request,pk=None):
    if(pk==None):
        articoli=Articolo.objects.all()
    else:
        articoli = Articolo.objects.filter(giornalista_id=pk)
    context ={
        'articoli':articoli,
    }
    return render(request, 'lista_articoli.html',context)

"""
nella prima versione le variabili a e g erano stringe le quali ad a tramite un ciclo 
venivano assegnati tutti i titoli degli articoli mentre a g tutti i nomi dei giornalisti
infine a e g venivano contecatenate in una variabile responde che che verra 
poi restituita con httpresponse() nella seconda versione a e g sono invece
due array nei quali vengono aggiungi nel primo i titoli degli articoli e nel
secondo i nomi dei giornalisti poi usando il metodo str aggiunto nelle classi 
nel models.py mettiamo nella variabile response a e g e restituiamo gli array con 
httpresponse()

"""
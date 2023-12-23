from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Articolo,Giornalista
import datetime
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


def giornalistaDetailView(request,pk):
    giornalista = get_object_or_404(Giornalista, pk=pk)
    context = {"giornalista": giornalista}
    return render(request, "giornalista_detail.html",context)


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

def query_base(request):
    pass
    #1. tutti gli articoli scritti da giornalisti con un certo cognome
    articoli_cognome=Articolo.objects.filter(giornalista__cognome='Rossi')
    
    #2. Totale
    numero_totale_articoli = Articolo.objects.count()

    #3. Contare il numero di articoli scritti da un giornalista specifico
    giornalista_1 = Giornalista.objects.get(id=3)
    numero_articoli_giornalista_1=Articolo.objects.filter(giornalista=giornalista_1).count()

    #4. Ordinare gli articoli per numero di articoli in ordine decrescente
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')

    #5. tutti gli articoli che non hanno visualizzazioni:
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)

    #6. articolo più visualizzato 
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()

    #7. tutti i giornalisti nati dopo una certa data
    giornalisti_data=Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990, 1, 1))

    #8. tutti gli articoli pubblicati in una data specifica
    articoli_del_giorno=Articolo.objects.filter(data=datetime.date(2023,1,1))

    #9. tutti gli articoli pubblicati in un intervallo di date
    articoli_periodo= Articolo.objects.filter(data__range=(datetime.date(2023, 1, 1), datetime.date(2023,12,31)))

    #10. gli articoli scritti da giornalisti prima del 1980
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980, 1, 1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)

    #11. il giornalista più giovane
    giornalista_giovane = Giornalista.objects.order_by('anno_di_nascita').first()

    #12. il giornalista più anziano
    giornalista_anziano = Giornalista.objects.order_by('-anno_di_nascita').first()

    #13. gli ultimi 5 articoli pubblicati
    ultimi = Articolo.objects.order_by('-data')[:5]

    #14. tutti gli articoli con un certo numero minimo di visualizzazioni
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)

    #15. tutti gli articoli che contengono una certa parola nel titolo
    articoli_parola = Articolo.objects.filter(titolo__icontains='importante')
    #16. articoli pubblicati in un certo mese di anno specifico
    #nota per poter modificare la data di un articolo togliere la proprietà auto_now=true al field data nel model
    #poi dare i comandi makemigration e migrate per abblicare le modifiche al database
    articoli_mese_anno=Articolo.objects.filter(data__month=1, data__year=2023)
    #17. giornalisti con almeno un articolo con più di 100 visualizzazioni
    giornalisti_con_articoli_popolari= Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct()
    #UTILIZZO DI PIU CONDIZIONI DI SELEZIONE
    data=datetime.date(1990,1,1)
    visualizzazioni=50
    #per mettere in AND le condizioni separarle con la virgola
    #18 ...scrivi quali articoli vengono selezionati
    articoli_con_and=Articolo.objects.filter(giornalista__anno_di_nascita__gt=data, visualizzazioni__gte=visualizzazioni)

    #per mettere le condizioni in OR utilizzare l'operatore Q
    from django.db.models import Q
    #19. scrivi quali articoli vengono selezionati
    articoli_con_or=Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt=data) |Q(visualizzazioni__lte=visualizzazioni))
    
    #per il not utilizzare l'operatore Q
    #20 ... scrivi quali articoli vengono selezionati
    #creare il dizionario context
    articoli_con_not= Articolo.objects.filter(~Q(giornalista__anno_di_nascita__lt=data))
    #oppure il metodo exclude
    # ... spiegala
    articoli_con_not = Articolo.objects.exclude(giornalista__anno_di_nascita__lt=data)
    #articolo.objects inizia dalla classe articolo exclude ritorna tutti i giornalisti tranne quelli la cui condizione risulta vera

    context = {
        'articolo_cognome': articoli_cognome,
        'numero_totale_articoli':numero_totale_articoli,
        'giornalista_1':giornalista_1,
        'numero_articoli_giornalista_1':numero_articoli_giornalista_1,
        'articoli_ordinati':articoli_ordinati,
        'articoli_senza_visualizzazioni':articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato':articolo_piu_visualizzato,
        'giornalisti_data':giornalisti_data,
        'articoli_del_giorno':articoli_del_giorno,
        'articoli_periodo':articoli_periodo,
        'giornalisti_nati':giornalisti_nati,
        'articoli_giornalisti':articoli_giornalisti,
        'giornalista_giovane':giornalista_giovane,
        'giornalista_anziano':giornalista_anziano,
        'ultimi':ultimi,
        'articoli_minime_visualizzazioni':articoli_minime_visualizzazioni,
        'articoli_parola':articoli_parola,
        'articoli_mese_anno':articoli_mese_anno,
        'giornalisti_con_articoli_popolari':giornalisti_con_articoli_popolari,
        'articoli_con_and':articoli_con_and,
        'articoli_con_or':articoli_con_or,
        'articoli_con_not':articoli_con_not,
    }
    return render(request, 'query.html',context)
 
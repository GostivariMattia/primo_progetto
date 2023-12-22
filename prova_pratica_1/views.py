from django.shortcuts import render
import random

# Create your views here.

def index_prova(request):
    return render(request,"index_prova.html")

def somma(request):
    var1=random.randint(1,10)
    var2=random.randint(1,10)
    context={
        'var1':var1,
        'var2':var2,
        'var_somma':var1+var2,

    }
    return render(request,"min_max.html",context)

def media(request):
    acc=0
    lista=[]
    for i in range(30):
        n=random.randint(1,10)
        lista.append(n)
        acc+=n
    media=(acc/len(lista))
    print(media)
    
    context={
        'lista':lista,
        'media':media,
        }
    
    return render(request,"media.html",context)

def voti(request):
    diz={'studente1':8,'studente2':5,'studente3':6,'studente4':7,}

    context={
        'voti':diz
    }

    return render(request,"voti.html",context)







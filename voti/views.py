from django.shortcuts import render

# Create your views here.

def viewA(request):
    materie=["Matematica","Italiano","Inglese","Storia","Geografia"]
    context={'materie':materie}
    return render(request, "viewA.html",context)


def homepage_voti(request):
    return render(request,"homepage_voti.html")

def viewB(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    context={'voti':voti}
    return render(request, "viewB.html",context)



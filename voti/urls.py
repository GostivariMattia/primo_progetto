from django.urls import path
from .views import homepage_voti,viewA,viewB

app_name='voti'

urlpatterns = [
    path('',homepage_voti,name='homepage_voti'),
    path('viewA/', viewA, name='viewA'),
    path('viewB/', viewB, name='viewB'),
    #path('viewC/', viewC, name=viewC),
    #path('viewD/', viewD, name=viewD),
]


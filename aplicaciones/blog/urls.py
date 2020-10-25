from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('lifeline/', lifeline, name='lifeline'),
    path('luz/', luz, name='luz'),
    path('fin/', fin, name='fin'),
    path('piedras/', piedras, name='piedras'),
    path('acuario/', acuario, name='acuario'),
    path('credo/', credo, name='credo'),
    path('biblia/', biblia, name='biblia'),
    path('libros/', libros, name='libros'),
    path('otros/', otros, name='otros'),
    path('<slug:slug>/', detallePost, name='detalle_post'),
]

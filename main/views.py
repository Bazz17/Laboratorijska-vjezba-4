# main/views.py
from django.shortcuts import render
from .models import Destinacija, Smjestaj, Rezervacija


def homepage(request):
    return render(request, 'homepage.html')

def destinacije_lista(request):
    destinacije = Destinacija.objects.all()
    return render(request, 'destinacije.html', {'destinacije': destinacije})

def smjestaji_lista(request):
    smestaji = Smjestaj.objects.all()
    return render(request, 'smjestaj_lista.html', {'smestaji': smestaji})

def rezervacije_lista(request):
    rezervacije = Rezervacija.objects.all()
    return render(request, 'rezervacija.html', {'rezervacije': rezervacije})

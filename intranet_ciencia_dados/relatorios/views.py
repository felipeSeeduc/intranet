from django.shortcuts import render
from django.http import HttpRequest

from .models import Relatorio

def relatorios(request: HttpRequest):
    relatorios = Relatorio.objects.all()
    return render(request, "relatorios/relatorios.html", {'relatorios': relatorios})

def relatorio(request: HttpRequest, id_relatorio):
    relatorio = Relatorio.objects.get(pk=id_relatorio)
    return render(request, "relatorios/relatorio.html", {'relatorio': relatorio})

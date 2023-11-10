from django.shortcuts import render
from django.http import HttpRequest


from .models import Tarefa

def tarefas(request: HttpRequest):
    tarefas = Tarefa.objects.all()
    tarefas_unique_status = set([(x.status, x.get_status_display()) for x in tarefas])    
    return render(request, "tarefas/tarefas.html", {'tarefas': tarefas, 'tarefas_unique_status': tarefas_unique_status})

def tarefa(request: HttpRequest, id_tarefa):
    tarefa = Tarefa.objects.get(pk=id_tarefa)
    return render(request, "tarefas/tarefa.html", {'tarefa': tarefa})

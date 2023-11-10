from django.urls import path
from . import views

# namespace = "relatorios"
urlpatterns = [
    path("", views.tarefas, name="tarefas"),
    path("tarefa/<int:id_tarefa>", views.tarefa, name="tarefa/<int:id_tarefa>"),
]
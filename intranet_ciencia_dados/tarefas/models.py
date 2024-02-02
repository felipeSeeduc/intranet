from django.db import models


class Tarefa(models.Model):

    STATUS_LIST = [
        ("done","Concluido"),
        ("in progress","Em progresso"),
        ("idle","Aguardando"),]

    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=STATUS_LIST, default="idle")
    log = models.TextField(default="")
    
    def __repr__(self) -> str:
        return f'Name: {self.name}'
    
    def __str__(self) -> str:
        return self.name
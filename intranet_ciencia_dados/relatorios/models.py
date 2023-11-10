from django.db import models

class Relatorio(models.Model):
    name = models.TextField(null=True, blank=True)
    iframe = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f'Name: {self.name}'
    
    def __str__(self) -> str:
        return self.name
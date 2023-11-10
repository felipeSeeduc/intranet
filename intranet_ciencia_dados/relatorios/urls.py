from django.urls import path
from . import views

# namespace = "relatorios"
urlpatterns = [
    path("", views.relatorios, name="relatorios"),
    path("relatorio/<int:id_relatorio>", views.relatorio, name="relatorio/<int:id_relatorio>"),
]
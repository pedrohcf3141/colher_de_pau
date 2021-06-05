from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display =('id', 'nome_receita', 'pessoa', 'categoria', 'publicada')
    list_editable = ('publicada','categoria')
    list_display_links=('id', 'nome_receita', 'pessoa')
    list_filter=('categoria', 'pessoa', 'publicada')
    search_fields=('nome_receita', 'categoria', 'pessoa__nome')
    list_per_page = 10

admin.site.register(Receita, ListandoReceitas)

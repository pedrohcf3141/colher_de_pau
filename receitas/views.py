import re
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Receita
from django.db.models import Q

def index(request):
    receitas = Receita.objects.order_by('-criado_em').filter(publicada=True)
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    cat_receitas = Receita.lista_categorias()
    receita_a_exibir = {
        'receita': receita,
        'cat_receitas': cat_receitas
    }
    return render(request, 'receita.html', receita_a_exibir)

def buscar(request):
    receitas = Receita.objects.order_by('-criado_em').filter(publicada=True)
    if 'buscar' in request.GET:
        busca = request.GET['buscar']
        receitas = receitas.filter(
            Q(nome_receita__icontains=busca) | 
            Q(categoria__icontains=busca)|
            Q(ingredientes__icontains=busca)
        )
    dados = {
        'receitas': receitas
    }
    return render(request, 'buscar.html', dados)
from pessoas.models import Pessoa
from django.db import models
from datetime import datetime
from pessoas.models import Pessoa


class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    criado_em = models.DateTimeField(default=datetime.now)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)

    def __str__(self) -> str:
        return self.nome_receita

    @property
    def lista_ingredientes(self):
        return [ingrediente for ingrediente in self.ingredientes.split('\n') ]
    
    @property
    def lista_passos(self):
        return [passo for passo in self.modo_preparo.split('\n') ]
    
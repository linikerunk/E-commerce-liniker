from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


# Create your views here.

class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Listar')
    

class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar Carrinho')


class RemoverDoCarrinho(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover do Carrinho')


class Carrinho(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')

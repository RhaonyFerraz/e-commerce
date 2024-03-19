from django.shortcuts import render
from .models import *
# Create your views here.


def homepage(request):
    banners = Banner.objects.filter(ativo=True)
    context = {"banners": banners}
    return render(request, 'homepage.html', context)


def loja(request, nome_categoria=None):
    print(nome_categoria)
    produtos = Produto.objects.filter(ativo=True)
    context = {"produtos": produtos}
    return render(request, 'loja.html', context)


def minha_conta(request):
    return render(request, 'usuario/minha_conta.html')


def login(request):
    return render(request, 'usuario/login.html')


def carrinho(request):
    return render(request, 'carrinho.html')


def checkout(request):
    return render(request, 'checkout.html')

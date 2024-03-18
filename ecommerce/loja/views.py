from django.shortcuts import render
from .models import *
# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def loja(request):
    produtos = Produto.objects.all()
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

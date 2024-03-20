from django.shortcuts import render
from .models import *
# Create your views here.


def homepage(request):
    banners = Banner.objects.filter(ativo=True)
    context = {"banners": banners}
    return render(request, 'homepage.html', context)


def loja(request, nome_categoria=None):
    produtos = Produto.objects.filter(ativo=True)
    if nome_categoria:
        produtos = produtos.filter(categoria__nome=nome_categoria)
    context = {"produtos": produtos}
    return render(request, 'loja.html', context)


def ver_produto(request, id_produto, id_cor=None):
    tem_estoque = False
    cores = {}
    tamanhos = {}
    nome_cor_selecionada = None
    if id_cor:
        cor = Cor.objects.get(id=id_cor)
        nome_cor_selecionada = cor.nome
    produto = Produto.objects.get(id=id_produto)
    itens_estoque = ItemEstoque.objects.filter(
        produto=produto, quantidade__gt=0)
    if len(itens_estoque) > 0:
        tem_estoque = True
        cores = {item.cor for item in itens_estoque}
        if id_cor:
            itens_estoque = ItemEstoque.objects.filter(
                produto=produto, quantidade__gt=0, cor__id=id_cor)
            tamanhos = {item.tamanho for item in itens_estoque}
    context = {"produto": produto, "itens_estoque": itens_estoque,
               "tem_estoque": tem_estoque, "cores": cores, "tamanhos": tamanhos, "nome_cor_selecionada": nome_cor_selecionada}
    return render(request, "ver_produto.html", context)


def minha_conta(request):
    return render(request, 'usuario/minha_conta.html')


def login(request):
    return render(request, 'usuario/login.html')


def carrinho(request):
    return render(request, 'carrinho.html')


def checkout(request):
    return render(request, 'checkout.html')

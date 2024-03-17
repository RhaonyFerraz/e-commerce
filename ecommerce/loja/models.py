from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_Length=200, nuLL=True, bLank=True)
    email = models.CharField(max_Length=200, nuLL=True, bLank=True)
    telefone = models.CharField(max_Length=200, nuLL=True, bLank=True)
    id_sessao = models.CharField(max_Length=200, nuLL=True, bLank=True)
    usuario = models.OneToOneField(
        User, nuLL=True, bLank=True, on_deLete=models.CASCADE)

# _Cliente
# nome
# email
# telefone
# usuario

# _produto
# imagem
# nome
# preço
# ativo
# categoria
# tipo

# _categoria (masculino, feminino, infantil)
# nome

# _tipos ( camisa, camiseta, bermuda, calça)
# nome

# _itemestoque
# produto ( ex ; camisa)
# tamanho ( ex ; p, m, g)
# cor (azul, verde, branco)
# quantidade

# _itenspedido
# itemestoque (camisa,laranja,M)
# quantidade  (10 itens)

# -Pedido
# cliente
# data_finalizacao
# finalizado
# id_transacao
# endereco
# itenspedido

# _endereco
# rua
# numero
# complemento
# cep
# cidade
# estado
# cliente

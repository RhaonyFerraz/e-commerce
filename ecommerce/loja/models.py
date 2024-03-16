from django.db import models

# Create your models here.


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

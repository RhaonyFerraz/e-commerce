from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="homepage"),
    path('loja/', loja, name="loja"),
    path('loja/<str:filtro>/', loja, name="loja"),
    path('produto/<int:id_produto>/', ver_produto, name="ver_produto"),
    path('produto/<int:id_produto>/<int:id_cor>/',
         ver_produto, name="ver_produto"),
    path('minhaconta/', minha_conta, name="minha_conta"),
    path('login/', login, name="login"),
    path('carrinho/', carrinho, name="carrinho"),
    path('checkout/', checkout, name="checkout"),
    path('adicionarcarrinho/<int:id_produto>/',
         adicionar_carrinho, name="adicionar_carrinho"),
    path('removercarrinho/<int:id_produto>/',
         remover_carrinho, name="remover_carrinho"),
    path('adicionarendereco/', adicionar_endereco, name="adicionar_endereco"),
]

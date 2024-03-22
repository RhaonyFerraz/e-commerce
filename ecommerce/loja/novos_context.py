from .models import Pedido, ItensPedido


def carrinho(request):
    quantidade_produtos_carrinho = 0
    if request.user.is_authenticated:
        cliente = request.user.cliente
    else:
        print("nao logado")
    pedido, criado = Pedido.objects.get_or_create(
        cliente=cliente, finalizado=False)
    # quantos pedidos tem no pedido do usuario
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)
    for item in itens_pedido:
        quantidade_produtos_carrinho += item.quantidade
    return {"quantidade_produtos_carrinho": quantidade_produtos_carrinho}

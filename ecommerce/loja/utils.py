

def filtrar_produtos(produtos, filtro):
    if filtro:
        if "-" in filtro:
            categoria, tipo = filtro.split("-")
            produtos = produtos.filter(
                tipo__slug=tipo, categoria__slug=categoria)
        else:

            produtos = produtos.filter(categoria__slug=filtro)
    return produtos

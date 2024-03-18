from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)


class Categoria(models.Model):  # Categorias (Masculino, Feminino, Infantil)
    nome = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.nome)


class Tipo(models.Model):  # Tipos (Camisa, Camiseta, Bermuda, Calça)
    nome = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.nome)


class Produto(models.Model):
    imagem = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(
        Tipo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Tipo: {self.tipo}, Preço: {self.preco}"


class ItemEstoque(models.Model):
    produto = models.ForeignKey(
        Produto, null=True, blank=True, on_delete=models.SET_NULL)
    cor = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=200, null=True, blank=True)
    quantidade = models.IntegerField(default=0)


class Endereco(models.Model):
    rua = models.CharField(max_length=400, null=True, blank=True)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cep = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    cliente = models.ForeignKey(
        Cliente, null=True, blank=True, on_delete=models.SET_NULL)


class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    finalizado = models.BooleanField(default=False)
    codigo_transacao = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.ForeignKey(
        Endereco, null=True, blank=True, on_delete=models.SET_NULL)
    data_finalizacao = models.DateTimeField(null=True, blank=True)


class ItensPedido(models.Model):
    item_estoque = models.ForeignKey(
        ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(
        Pedido, null=True, blank=True, on_delete=models.SET_NULL)

    class Banner(models.Model):
        imagem = models.ImageField(null=True, blank=True)
        link_destino = models.CharField(max_length=400, null=True, blank=True)
        ativo = models.BooleanField(default=False)

        def __str__(self):
            return f"{self.link_destino} - Ativo: {self.ativo}"

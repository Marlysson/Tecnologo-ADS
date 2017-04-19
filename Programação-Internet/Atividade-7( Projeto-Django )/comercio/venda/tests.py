
from django.test import TestCase

from model_mommy import mommy

from .models import Cliente, Fornecedor, Produto, Pedido, ItemPedido, Venda,  \
    ItemVenda

from datetime import date, timedelta
import unittest


fixture_cliente = {
    "cpf": "123.123.123-23",
    "nome": "Marlysson",
    "endereco": "Endereço 1",
    "complemento": "Complemento 1",
    "cidade": "Teresina",
    "estado": "PI",
    "cep": "64079-020",
    "fone_residencial": "3232-3232",
    "fone_trabalho": "1234-1234",
    "renda_familiar": 2500,
    "email": "marlysson5@gmail.com"
}

fixture_fornecedor = {
    "cnpj": "22.333.444/4345-32",
    "nome": "Armazém Paraíba",
    "endereco": "Endereço 2",
    "complemento": "Complemento 2",
    "cidade": "São Paulo",
    "estado": "SP",
    "cep": "64077-044",
    "fone": "3434-4444",
    "responsavel": "José Fernandes",
    "website": "http://www.armazemparaiba.com"
}


fixture_produto_livro = {
    "nome_produto": "Não conte à ninguém",
    "quantidade": 100,
    "min_quantidade": 10
}

fixture_produto_cd = {
    "nome_produto": "Skillet - Invencible",
    "quantidade": 200,
    "min_quantidade": 20
}


class TestCliente(TestCase):

    def setUp(self):

        self.cliente = Cliente.objects.create(**fixture_cliente)
        self.fornecedor = Fornecedor.objects.create(**fixture_fornecedor)

    def tearDown(self):

        Cliente.objects.all().delete()
        Fornecedor.objects.all().delete()
        Produto.objects.all().delete()

    def test_deve_criar_um_cliente(self):
        self.assertEquals(1, self.cliente.id)

    def test_deve_criar_um_fornecedor(self):
        self.assertEquals(1, self.fornecedor.id)

    def test_deve_criar_produtos(self):

        arroz = Produto.objects.create(
            nome_produto="Arroz",
            quantidade=100,
            min_quantidade=10)

        feijao = Produto.objects.create(
            nome_produto="Feijão",
            quantidade=200,
            min_quantidade=20)

        self.assertEquals(1, arroz.codigo_produto)
        self.assertEquals(2, feijao.codigo_produto)

    def test_deve_criar_um_pedido_para_um_fornecedor(self):

        pedido = Pedido.objects.create(
            data_pedido=date.today(),
            data_recebimento=date.today() + timedelta(days=10),
            preco_total=0,
            codigo_fornecedor=self.fornecedor,
        )

        self.assertEquals(1, pedido.codigo)

    def test_deve_adicionar_itens_a_pedido(self):

        produto_livro = Produto.objects.create(**fixture_produto_livro)
        produto_cd = Produto.objects.create(**fixture_produto_cd)

        pedido = Pedido.objects.create(
            data_pedido=date.today(),
            data_recebimento=date.today() + timedelta(days=10),
            preco_total=0,
            codigo_fornecedor=self.fornecedor,
        )

        item_livro = ItemPedido.objects.create(
            codigo_pedido=pedido,
            codigo_produto=produto_livro,
            preco_unitario=15.0,
            quantidade=2
        )

        item_cd = ItemPedido.objects.create(
            codigo_pedido=pedido,
            codigo_produto=produto_cd,
            preco_unitario=150.00,
            quantidade=2
        )

        pedido.adicionar_item(item_livro)

        self.assertEquals(pedido.preco_total, 30.00)

        pedido.adicionar_item(item_cd)

        self.assertEquals(pedido.preco_total, 330.00)

    def test_deve_criar_uma_venda_corretamente(self):

        venda = Venda.objects.create(
            data_venda=date.today(),
            valor_total=0,
            codigo_cliente=self.cliente
        )

        self.assertEquals(1, venda.codigo_venda)

    def test_deve_criar_uma_venda_inserindo_seus_itens(self):

        produto_livro = Produto.objects.create(**fixture_produto_livro)
        produto_cd = Produto.objects.create(**fixture_produto_cd)

        venda = Venda.objects.create(
            data_venda=date.today(),
            valor_total=0,
            codigo_cliente=self.cliente
        )

        item_livro = ItemVenda.objects.create(
            codigo_venda=venda,
            codigo_produto=produto_livro,
            preco_unitario=25.0,
            quantidade=2
        )

        item_cd = ItemVenda.objects.create(
            codigo_venda=venda,
            codigo_produto=produto_cd,
            preco_unitario=50.0,
            quantidade=10
        )

        for item in [item_livro, item_cd]:
            venda.adicionar_item(item)

        quantidade_itens_venda = ItemVenda.objects.filter(
            codigo_venda=venda).count()

        self.assertEquals(quantidade_itens_venda,2)

        self.assertEquals(550, venda.valor_total)
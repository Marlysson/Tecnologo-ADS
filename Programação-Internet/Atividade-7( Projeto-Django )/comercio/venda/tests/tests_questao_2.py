
from django.test import TestCase

from venda.fixtures import *

from venda.models import Cliente, Fornecedor, Produto, Pedido, ItemPedido, Venda,  \
    ItemVenda

from datetime import date, timedelta
import unittest


class TestsSegundaQuestao(TestCase):

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

        pedido.refresh_from_db()
        
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

        quantidade_itens_venda = ItemVenda.objects.filter(
            codigo_venda=venda).count()


        self.assertEquals(quantidade_itens_venda, 2)

        venda.refresh_from_db()
        self.assertEquals(550, venda.valor_total)
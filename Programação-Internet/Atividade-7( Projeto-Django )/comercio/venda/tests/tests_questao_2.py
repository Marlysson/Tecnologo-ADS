# -*- coding : utf-8 -*-

from django.test import TestCase
from django.db.models import Sum

from venda.fixtures import fixture_cliente, fixture_produto_cd, \
    fixture_produto_livro , fixture_fornecedor

from venda.models import Cliente, Fornecedor, Produto, Venda, ItemVenda, ItemPedido, Pedido

from datetime import date


class TestsSegundaQuestao(TestCase):

    def test_deve_retornar_todos_os_clientes_cadastrados(self):

        for indice in range(1, 6):
            Cliente.objects.create(**fixture_cliente)

        quantidade_clientes = Cliente.objects.all().count()

        self.assertEquals(5, quantidade_clientes)

    def test_deve_retornar_todas_as_venda_de_um_cliente(self):

        cliente = Cliente.objects.create(**fixture_cliente)

        produto_livro = Produto.objects.create(**fixture_produto_cd)
        produto_cd = Produto.objects.create(**fixture_produto_livro)

        # Primeira compra do cliente

        venda_1 = Venda.objects.create(
            data_venda=date.today(),
            valor_total=0,
            codigo_cliente=cliente)

        item_cd = ItemVenda.objects.create(
        	codigo_venda=venda_1,
            codigo_produto=produto_cd,
            preco_unitario=25,
            quantidade=3)

        item_livro = ItemVenda.objects.create(
        	codigo_venda=venda_1,
            codigo_produto=produto_cd,
            preco_unitario=20,
            quantidade=5)

        # Segunda compra do Cliente

        venda_2 = Venda.objects.create(
            data_venda=date.today(),
            valor_total=0,
            codigo_cliente=cliente)

        item_cd_2 = ItemVenda.objects.create(
        	codigo_venda=venda_2,
            codigo_produto=produto_cd,
            preco_unitario=50,
            quantidade=5)

        item_livro_2 = ItemVenda.objects.create(
        	codigo_venda=venda_2,
            codigo_produto=produto_livro,
            preco_unitario=25,
            quantidade=2)

        quantidade_compras = cliente.minhas_compras.all().count()

        self.assertEquals(quantidade_compras, 2)

        # Compra 1
        venda_1.refresh_from_db()
        self.assertEquals(venda_1.valor_total,175)

        #Compra 2
        venda_2.refresh_from_db()
        self.assertEquals(venda_2.valor_total,300)

        valor_das_compras = sum(cliente.minhas_compras.all().values_list("valor_total",flat=True))

        self.assertEquals(valor_das_compras, 475)

    def test_deve_retornar_um_pedido(self):

    	from datetime import date , timedelta

    	fornecedor = Fornecedor.objects.create(**fixture_fornecedor)
    	produto = Produto.objects.create(**fixture_produto_cd)

    	pedido = Pedido.objects.create(
    		data_pedido=date.today(),
    		data_recebimento=date.today() + timedelta(days=2),
    		preco_total=0,
    		codigo_fornecedor=fornecedor
    	)

    	item_pedido = ItemPedido.objects.create(
    		codigo_pedido=pedido,
    		codigo_produto=produto,
    		preco_unitario=50,
    		quantidade=2
    	)

    	pedido = Pedido.objects.get(pk=pedido.pk)

    	self.assertEquals(1,pedido.codigo)

    def test_deve_todos_os_itens_de_um_pedido(self):

    	from datetime import date , timedelta

    	fornecedor = Fornecedor.objects.create(**fixture_fornecedor)
    	cd = Produto.objects.create(**fixture_produto_cd)
    	livro = Produto.objects.create(**fixture_produto_livro)

    	pedido = Pedido.objects.create(
    		data_pedido=date.today(),
    		data_recebimento=date.today() + timedelta(days=2),
    		preco_total=0,
    		codigo_fornecedor=fornecedor
    	)

    	livros = ItemPedido.objects.create(
    		codigo_pedido=pedido,
    		codigo_produto=livro,
    		preco_unitario=50,
    		quantidade=2
    	)

    	cds = ItemPedido.objects.create(
    		codigo_pedido=pedido,
    		codigo_produto=cd,
    		preco_unitario=40,
    		quantidade=3
    	)

    	itens = pedido.itens.all()

    	queryset_dos_itens = []

    	queryset_dos_itens.append('<ItemPedido: Produto=(nome=Não conte à ninguém, estoque=100), total=100.00>')
    	queryset_dos_itens.append('<ItemPedido: Produto=(nome=Skillet - Invincible, estoque=200), total=120.00>')

    	self.assertQuerysetEqual(list(itens),queryset_dos_itens)
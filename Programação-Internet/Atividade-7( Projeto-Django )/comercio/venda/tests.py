
from django.test import TestCase

from model_mommy import mommy

from .models import Cliente, Fornecedor, Produto, Pedido, ItemPedido, Venda

from datetime import date

class TestCliente(TestCase):

    def test_deve_criar_um_cliente(self):

        cliente = Cliente.objects.create(
            cpf="123.123.123-23",
            nome="Marlysson",
            endereco="Endereço 1",
            complemento="Complemento 1",
            cidade="Teresina",
            estado="PI",
            cep="64079-020",
            fone_residencial="3232-3232",
            fone_trabalho="1234-1234",
            renda_familiar=2500,
            email="marlysson5@gmail.com")

        cliente.full_clean()

        self.assertEquals(1, cliente.id)

    def test_deve_criar_um_fornecedor(self):

        fornecedor = Fornecedor.objects.create(
            cnpj="22.333.444/4345-32",
            nome="Armazém Paraíba",
            endereco="Endereço 2",
            complemento="Complemento 2",
            cidade="São Paulo",
            estado="SP",
            cep="64077-044",
            fone="3434-4444",
            responsavel="José Fernandes",
            website="http://www.armazemparaiba.com")

        fornecedor.full_clean()

        self.assertEquals(1, fornecedor.id)

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

        from datetime import date, timedelta

        self.fornecedor = mommy.make(Fornecedor)

        pedido = Pedido.objects.create(
            data_pedido=date.today(),
            data_recebimento=date.today() + timedelta(days=10),
            preco_total=0,
            codigo_fornecedor=self.fornecedor,
        )

        self.assertEquals(1, pedido.codigo)

    def test_deve_adicionar_itens_a_pedido(self):

        from datetime import date, timedelta

        self.fornecedor = mommy.make(Fornecedor)
        self.produtos = mommy.make(Produto, 2)

        pedido = Pedido.objects.create(
            data_pedido=date.today(),
            data_recebimento=date.today() + timedelta(days=10),
            preco_total=0,
            codigo_fornecedor=self.fornecedor,
        )

        livro = ItemPedido.objects.create(
            codigo_pedido=pedido,
            codigo_produto=self.produtos[0],
            preco_unitario=15.0,
            quantidade=2
        )

        cd_videogame = ItemPedido.objects.create(
            codigo_pedido=pedido,
            codigo_produto=self.produtos[1],
            preco_unitario=150.00,
            quantidade=2
        )

        pedido.adicionar_item(livro)

        self.assertEquals(pedido.preco_total, 30.00)

        pedido.adicionar_item(cd_videogame)

        self.assertEquals(pedido.preco_total, 330.00)

    def test_deve_criar_uma_venda_corretamente(self):

        cliente = mommy.make(Cliente)

        venda = Venda.objects.create(
            data_venda=date.today(),
            valor_total=0,
            codigo_cliente=cliente
        )

        self.assertEquals(1, venda.codigo_venda)


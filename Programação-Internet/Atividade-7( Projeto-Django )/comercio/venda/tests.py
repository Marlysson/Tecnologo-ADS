
from django.test import TestCase

from .models import Cliente , Fornecedor , Produto

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

		self.assertEquals(1,cliente.id)

	def test_deve_criar_um_fornecedor(self):

		fornecedor = Fornecedor.objects.create(
			cnpj="",
			nome="Armazém Paraíba",
			endereco="Endereço 2",
			complemento="Complemento 2",
			cidade="São Paulo",
			estado="SP",
			cep="64077-044",
			fone="3434-4444",
			responsavel="José Fernandes",
			website="www.armazemparaiba.com")

		self.assertEquals(1,fornecedor.id)


	def test_deve_criar_produtos(self):

		arroz = Produto.objects.create(
			nome_produto="Arroz",
			quantidade=100,
			min_quantidade=10)

		feijao = Produto.objects.create(
			nome_produto="Feijão",
			quantidade=200,
			min_quantidade=20)

		self.assertEquals(1,arroz.codigo_produto)
		self.assertEquals(2,feijao.codigo_produto)
from django.contrib import admin

from .models import Cliente, Fornecedor, Produto, Pedido, ItemPedido, Venda


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["cpf", "nome", "endereco",
                    "cidade", "estado", "cep", "email"]

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ["cnpj", "nome", "cep", "fone", "website"]


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["data_pedido", "data_recebimento",
                    "preco_total", "codigo_fornecedor"]

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ["nome_produto","quantidade"]
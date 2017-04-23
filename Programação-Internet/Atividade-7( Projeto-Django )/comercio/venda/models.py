
from django.db import models
from django.core.validators import RegexValidator
from datetime import date


class Cliente(models.Model):

    validador_cpf = RegexValidator("^\d{3}\.\d{3}\.\d{3}-\d{2}$")
    validador_cep = RegexValidator("^\d{5}-\d{3}$")
    validador_fone = RegexValidator("^\d{4}-\d{4}$")

    cpf = models.CharField(max_length=14, validators=[
                           validador_cpf], blank=False, null=False)
    nome = models.CharField(max_length=30, blank=False, null=False)
    endereco = models.TextField(max_length=35, blank=False, null=False)
    complemento = models.TextField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9, validators=[validador_cep])
    fone_residencial = models.CharField(
        max_length=9, validators=[validador_fone])
    fone_trabalho = models.CharField(max_length=9, validators=[validador_fone])
    renda_familiar = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(max_length=50)

    class Meta:
        db_table = 'cliente'

    def __repr__(self):
        return "{}, {}".format(self.cpf, self.nome)


class Fornecedor(models.Model):

    validador_cpnj = RegexValidator("\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}")
    validador_fone = RegexValidator("^\d{4}-\d{4}$")
    validador_cep = RegexValidator("^\d{5}-\d{3}$")

    cnpj = models.CharField(max_length=20, validators=[
                            validador_cpnj], null=False, blank=False)
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=35)
    complemento = models.CharField(max_length=50)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9, validators=[validador_cep])
    fone = models.CharField(max_length=9, validators=[validador_fone])
    responsavel = models.CharField(max_length=30)
    website = models.URLField()

    class Meta:
        db_table = 'fornecedor'

    def __str__(self):
        return "{}".format(self.nome)


class Pedido(models.Model):

    codigo = models.AutoField(primary_key=True)
    data_pedido = models.DateField()
    data_recebimento = models.DateField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_fornecedor = models.ForeignKey(
        Fornecedor, related_name="meus_pedidos")

    class Meta:
        db_table = 'pedido'

    def __str__(self):
        return "data={}, preco_total={}".format(self.codigo_venda, date.strftime(self.data_pedido, "%d/%m/%Y"), self.preco_total)


class Produto(models.Model):

    codigo_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=35)
    quantidade = models.IntegerField()
    min_quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return "nome={}, estoque={}".format(self.nome_produto, self.quantidade)


class Venda(models.Model):

    codigo_venda = models.AutoField(primary_key=True)
    data_venda = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_cliente = models.ForeignKey(Cliente, related_name="minhas_compras")

    class Meta:
        db_table = 'venda'

    def __str__(self):
        return "data={}, preco_total={}".format(self.codigo_venda, date.strftime(self.data_venda, "%d/%m/%Y"), self.valor_total)


class ItemVenda(models.Model):

    codigo_venda = models.ForeignKey(Venda, related_name="itens")
    codigo_produto = models.ForeignKey(Produto, related_name="itens_vendidos")
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    class Meta:
        db_table = 'item_venda'

    def save(self, *args, **kwargs):

        from decimal import Decimal

        venda = Venda.objects.get(pk=self.codigo_venda.pk)

        venda.valor_total += Decimal(self.preco_unitario) * self.quantidade
        venda.save()

        super(ItemVenda, self).save(*args, **kwargs)

    def __str__(self):
        return "{}, {}".format(self.codigo_produto, self.preco_unitario, self.quantidade)


class ItemPedido(models.Model):

    codigo_pedido = models.ForeignKey(Pedido, related_name="itens")
    codigo_produto = models.ForeignKey(Produto, related_name="itens_produto")
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def save(self, *args, **kwargs):

        from decimal import Decimal

        pedido = Pedido.objects.get(pk=self.codigo_pedido.pk)
        pedido.preco_total += Decimal(self.preco_unitario) * self.quantidade
        pedido.save()

        super(ItemPedido, self).save(*args, **kwargs)

    class Meta:
        db_table = 'item_pedido'

    def __str__(self):
        return "Produto=({}), total={}".format(self.codigo_produto, self.preco_unitario*self.quantidade)

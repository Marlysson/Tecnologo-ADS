from django.db import models
from django.core.validators import RegexValidator

class Cliente(models.Model):

	validador_cpf = RegexValidator(regex="^\d{3}\.\d{3}\.\d{3}-\d{2}$")
	validador_cep = RegexValidator(regex="^\d{5}-\d{3}$")
	validador_fone = RegexValidator(regex="^\d{4}-\d{4}$")

	cpf = models.CharField(max_length=14,validators=[validador_cpf],blank=False,null=False)
	nome = models.CharField(max_length=30,blank=False,null=False)
	endereco = models.TextField(max_length=35,blank=False,null=False)
	complemento = models.TextField(max_length=50,blank=True,null=True)
	cidade = models.CharField(max_length=25)
	estado = models.CharField(max_length=2)
	cep = models.CharField(max_length=8,validators=[validador_cep])
	fone_residencial = models.CharField(max_length=9,validators=[validador_fone])
	fone_trabalho = models.CharField(max_length=9,validators=[validador_fone])
	renda_familiar = models.DecimalField(max_digits=10,decimal_places=2)
	email = models.EmailField()

	def __repr__(self):
		return "<Cliente {} , {}>".format(self.cpf,self.nome)


class Fornecedor(models.Model):

	cnpj = models.CharField(max_length=20)
	nome = models.CharField(max_length=30)
	endereco = models.CharField()
	complemento = models.CharField()
	cidade = models.CharField()
	estado = models.CharFeld()
	cep = models.CharField()
	fone_trabalho = models.CharField()
	responsavel = models.CharField()
	website= models.URLField()
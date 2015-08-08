# -*- coding:utf-8 -*-

class Algebra(object):

	'''
	Classe para tratar operações que envolvem Álgebra Linear
	'''

	def valida_escalar(self,valor):
		if type(valor) == int or type(valor) == float:
			return True
		return False

	def valida_vetor(self,vetor):
		if type(vetor) == list:
			for item in vetor:
				if type(item) == str:
					return False #Encontrou uma string
			return True # Nenhum item é string
		return False # Não é vetor

	def somar_vetores(self,vetor1,vetor2):

		soma = []
		for posicao,item_vt1 in enumerate(vetor1):
			soma.append(item_vt1 + vetor2[posicao])

		return soma

	def graus(self,radiano):
		from math import pi

		return radiano * (180 / pi)
		
	def produto_por_escalar(self,escalar,vetor):
		result = []
		
		for posicao,valor in enumerate(vetor):
			result.append(escalar*valor)
		return result

	def produto_escalar(self,vetor1,vetor2):

		produto = []

		for posicao,item in enumerate(vetor1):
			produto.append(item*vetor2[posicao])

		return sum(produto)

	def angulo(self,vetor1,vetor2):
		
		from math import acos

		produto_escalar = self.produto_escalar(vetor1,vetor2)
		produto_magnitude = self.magnitude(vetor1) * self.magnitude(vetor2)

		cosseno = produto_escalar / produto_magnitude

		return self.graus(acos(cosseno))

	def magnitude(self,vetor):
		from math import sqrt

		soma_itens = sum([item**2 for item in vetor])
		magnitude = sqrt(soma_itens)

		return magnitude

	def normalizar(self,vetor):
		magnitude = self.magnitude(vetor)

		return ['{:.2f}'.format(item/magnitude) for item in vetor]

	def inverter(self,vetor):
		return [item*(-1) for item in vetor]

		
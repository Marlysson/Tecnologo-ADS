# -*- coding : utf-8 -*-

def soma(valor_1,valor_2):
	return valor_1 + valor_2

def subtracao(valor_1,valor_2):
	return valor_1 - valor_2

def divisao(soma,subtracao):
	return soma / float(subtracao)

def resultado(valor_1 , valor_2):
	return divisao( soma(valor_1,valor_2) , subtracao(valor_1,valor_2) )

print(resultado(10,4))
# -*- coding: utf-8 -*-

'''
Criar um algoritmo que calcule e imprima o valor de b^n.
O valor de n deverá ser maior que 1 e inteiro e o valor de
b maior ou igual a 2 e inteiro.
'''

n = int(input('Valor de b: '))
b = int(input("Valor de n: "))

if isinstance(n,int) and n >= 1:
	if isinstance(b,int) and b >= 2:
		print("Resultado de b^n: ",b**n)
	else:
		print("O valor do b não está correto.")
else:
	print("O valor de n não está correto.")

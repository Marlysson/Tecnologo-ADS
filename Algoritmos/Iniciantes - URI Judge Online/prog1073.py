# -*- coding:utf8 -*-

numero = int(input('Número: '))

if numero % 2 == 0:
	numero += 1

quadrados = [i**2 for i in range(2,numero,2)]
numero 	  = [i for i in range(2,numero,2)]

for numero,quadrado in zip(numero,quadrados):
	print '{}^{} = {}'.format(numero,numero,quadrado)
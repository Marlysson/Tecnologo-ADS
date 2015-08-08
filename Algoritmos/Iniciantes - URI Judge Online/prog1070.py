# -*- coding:utf8 -*-

numero = int(input('Digite um número: '))
cont_numeros = 0

if numero % 2 == 0:
	atual = numero+1
else:
	atual = numero

while cont_numeros != 6:
	print atual
	atual +=2
	cont_numeros+=1
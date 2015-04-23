# -*- coding:utf-8 -*-

numeros = []

for i in range(5):
	numeros.append(input('Numero: '))

def par(x):
	return x%2==0

pares = filter(par,numeros)
# pares = [i for i in numeros if i%2 == 0]

print '{} números pares.'.format(len(pares))
# -*- coding :utf8 -*-
numeros = []

for i in range(6):
	num = float(input('Numero: '))
	numeros.append(num)

#Primeira forma
# def positivo(n):
# 	return n > 0

# positivos = len(filter(positivo,numeros))

#Segunda forma

positivos = len([int(i) for i in numeros if i > 0])

print '{} valores positivos'.format(positivos)
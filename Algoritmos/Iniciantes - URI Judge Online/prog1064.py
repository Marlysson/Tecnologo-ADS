# -*- coding :utf8 -*-

numeros = []

for i in range(6):
	numeros.append(input('Numero: '))

def positivos(x):
	return x > 0

positivos = filter(positivos,numeros)

print '{} valores positivos'.format(len(positivos))
print '{}'.format(float(sum(positivos)/len(positivos))) 
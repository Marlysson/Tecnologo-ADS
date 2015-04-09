# -*- coding:utf-8 -*-

numeros = []
pares,impares,positivos,negativos = 0,0,0,0

for i in range(5):
	numeros.append(int(input('Número: ')))

for i in numeros:
	if i % 2 == 0:
		pares += 1
	else:
		impares += 1
	if i > 0:
		positivos += 1
	else:
		negativos += 1

print '{} numeros pares'.format(pares)
print '{} numeros impares'.format(impares)
print '{} numeros positivos'.format(positivos)
print '{} numeros negativos'.format(negativos)
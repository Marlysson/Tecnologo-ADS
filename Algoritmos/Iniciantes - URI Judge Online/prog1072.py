# -*- coding:utf8 -*-

numeros = []
vezes = int(input('Quantidade de testes: '))
dentro,fora = 0,0

for i in range(vezes):
	numeros.append(int(input('Número: ')))
	if 10 <= numeros[i] <= 20:
		dentro += 1
	else:
		fora += 1
		
print '{} in'.format(dentro)
print '{} out'.format(fora)

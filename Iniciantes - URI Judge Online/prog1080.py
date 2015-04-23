# -*- coding:utf8 -*-

'''
Leia 100 valores inteiros. Apresente então o maior valor lido 
e a posição dentre os 100 valores lidos.
'''

import random

numeros = random.sample(xrange(1,100000),100)

maior = 0
for i in numeros:
	if i >= maior:
		maior = i

print 'Maior: {}'.format(maior)
print 'Posição: {}º'.format(numeros.index(maior))


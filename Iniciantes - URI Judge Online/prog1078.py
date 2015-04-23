# -*- coding : utf8 -*-
'''
Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
1 x N = N      2 x N = 2N        ...       10 x N = 10N
'''
numero = int(input('Numero: '))

for i in range(1,11):
	print '{} x {} = {}'.format(i,numero,i*numero)
# -*- coding: utf-8 -*-

'''
Criar um algoritmo que leia um número (n) e imprima a soma
dos números múltiplos de 5 no intervalo aberto
entre 1 e num. Suponha que n será maior que 1.
'''

n = int(input("Número: "))

soma = 0

for i in range(1,n):
	if i % 5 == 0:
		soma += i
print(soma)		

# -*- coding:utf-8 -*-

'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa
um valor monetário.A seguir, calcule o menor número de notas e moedas 
possíveis no qual o valor pode ser decomposto.As notas consideradas 
são de 100, 50, 20, 10, 5, 2.As moedas possíveis são de 1, 0.50, 
0.25,0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

'''
valor = float(input('Valor para trocar: '))

print 'CÉDULAS:'
for i in [100,50,20,10,5,2]:
	notas = valor // i
	valor -= notas*i
	print '{} Notas de R$ {:.2f}'.format(int(notas),i)
	

print '\nMOEDAS:'
for i in [1,0.50,0.25,0.10,0.05,0.01]:
	notas = valor // i
	valor -= notas*i
	print '{} moedas de R$ {:.2f}'.format(int(notas),i)

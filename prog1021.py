# -*- coding:utf-8 -*-

'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa
um valor monetário.A seguir, calcule o menor número de notas e moedas 
possíveis no qual o valor pode ser decomposto.As notas consideradas 
são de 100, 50, 20, 10, 5, 2.As moedas possíveis são de 1, 0.50, 
0.25,0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

'''

valor_total = float(input('Valor para trocar: '))

notas = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
valores_cedulas = {}

for i in notas:
	if valor_total >= i:
		quant_notas = valor_total // i
		valores_cedulas[i] = int(quant_notas)
		valor_total %= i
	else:
		valores_cedulas[i] = 0
		
cedulas = [i for i in notas if i >= 2]
moedas  = [i for i in notas if i < 2]

print '\nCÉDULAS:'
for i in cedulas:
	print '%d cédula(s) de R$ %.2f' % (valores_cedulas[i],i) 
print '\nMOEDAS:'
for i in moedas:
	print '%d moedas(s) de R$ %.2f' %(valores_cedulas[i],i) 
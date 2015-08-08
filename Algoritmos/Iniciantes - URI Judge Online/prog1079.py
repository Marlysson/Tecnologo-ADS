# -*- coding:utf8 -*-
'''
Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir.
Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal.
Apresente a média ponderada para cada um destes conjuntos de 3 valores,sendo que o 
primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.
'''

medias = []
testes = int(input('Testes: '))

for i in range(testes):
	dados = raw_input('Números: ').split()
	dados = [float(i) for i in dados]
	
	media = (dados[0]*2 + dados[1]*3 + dados[2]*5) / 10
	medias.append(media)

for i in medias:
	print '{:.1f}'.format(i)
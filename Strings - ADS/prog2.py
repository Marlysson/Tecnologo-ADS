# -*- coding:utf8 -*-

def conta_letra(palavra,letra):
	cont = 0
	for i in palavra:
		if i == letra:
			cont += 1
	return cont
	#return palavra.count(letra)


print conta_letra('Marlysson','s')


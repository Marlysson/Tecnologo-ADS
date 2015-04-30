# -*- coding:utf8 -*-

def conta_letra(palavra,letra):
	
	#Manualmente
	cont = 0
	for i in palavra:
		if i == letra:
			cont += 1
	# return cont

	#Compreensão de Listas
	cont = len([i for i in palavra if i == letra])
	return cont
	
	#Pythônica
	#return palavra.count(letra)
	# return cont


print conta_letra('Marlysson','s')


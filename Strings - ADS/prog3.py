# -*- coding:utf8 -*-

def apaga_caractere(palavra,letra):
	
	#Manualmente
	palavra = list(palavra)
	
	for i in palavra:
		if i == letra:
			palavra[palavra.index(i)] = ''
	return ''.join(palavra)

	#Pythônica
	# return palavra.replace(letra,'')


print apaga_caractere('Marlysson','y')
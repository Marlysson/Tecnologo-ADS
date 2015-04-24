# -*- coding:utf8 -*-

def contida(palavra1,palavra2):
	#Pythônica
	if palavra1 in palavra2:
		return 'Contem'
	return 'Nao contem'

	#Manualmente
	cont = 0
	if len(palavra1) <= len(palavra2):
		for i in range(0,len(palavra2)+1):
			if palavra2[i:i+len(palavra1)] == palavra1:
				return 'Contem'
		return 'Nao Contem'
	else:
		return 'Nao Contem'


print contida('asa','casa')

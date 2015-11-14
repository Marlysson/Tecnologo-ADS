# -*- coding:utf8 -*-

def contida(palavra1,palavra2):
	#Pythônica
	# if palavra1 in palavra2:
	# 	return 'Contem'
	# return 'Nao contem'

	# Manualmente
	cont = 0
	if len(palavra1) <= len(palavra2):
		for i in range(0,len(palavra2)+1):
			#Percorre cada espaço da string com o tamanho da string menor
			#Ex:asa,casade => cas,asa,sad,ade **utilizar combinações
			if palavra2[i:i+len(palavra1)] == palavra1:
				return 'Contém'
		return 'Nao Contém'
	else:
		return 'Palavra1 maior que palavra2'


print contida('nolar','otorrinolaringologista')

# -*- coding : utf-8 -*-

def Mensagem():
	x = 10
	y = 1
	x -= 1
	y += 2
	x = x - 1
	y = y + 2
	x = x - 1
	y = y + 2
	
	# Nesse momendo o valor das variáveis são:
	# x: 7 ; y: 7; 
	# x e y ficaram iguais

	if x > y:
		return "x ficou maior que y"
	elif x < y:
		return "x ficou menor que y"
	else:
		return "x e y ficaram iguais"

print(Mensagem())
# -*- coding : utf-8 -*-

# Mensagem: Positivo , Negativo ou igual a zero

def modularidade(num):
	if num > 0:
		return 'Positivo'
	elif num < 0:
		return 'Negativo'
	return 'Igual a zero'

assert modularidade(10) == 'Positivo'
assert modularidade(-2) == 'Negativo'
assert modularidade(0) == 'Igual a zero'
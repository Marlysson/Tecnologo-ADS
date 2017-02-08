# -*- coding : utf-8 -*-

# Retornar verdadeiro se foi digitado uma vogal

def isVogal(letra):
	if letra == 'a' or \
	   letra == 'e' or \
	   letra == 'i' or \
	   letra == 'o' or \
	   letra == 'u':
	   return True
	return False

assert isVogal('a') == True
assert isVogal('b') == False
assert isVogal('c') == False
assert isVogal('d') == False
assert isVogal('e') == True
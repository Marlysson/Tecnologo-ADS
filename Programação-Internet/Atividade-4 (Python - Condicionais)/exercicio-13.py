# -*- coding : utf-8 -*-

# Múltiplo de 2 e 3

from is_multiplo import is_multiplo

def mostra_mensagem(num):
	if is_multiplo(num,2) and is_multiplo(num,3):
		return 'Verdadeiro'
	return 'Falso'

assert mostra_mensagem(3) == 'Falso'
assert mostra_mensagem(6) == 'Verdadeiro'
assert mostra_mensagem(14) == 'Falso'
assert mostra_mensagem(12) == 'Verdadeiro'
# -*- coding : utf-8 -*-

# Mensagem se é multiplo de 7 ou não

from is_multiplo import is_multiplo

def isMultiplo7(num):
	return is_multiplo(num,7)

def mostra_mensagem(num):
	template = 'O número{}múltiplo de 7.'

	if isMultiplo7(num):
		return template.format(' é ')
	return template.format(' não é ')


assert mostra_mensagem(7) == 'O número é múltiplo de 7.'
assert mostra_mensagem(14) == 'O número é múltiplo de 7.'
assert mostra_mensagem(16) == 'O número não é múltiplo de 7.'
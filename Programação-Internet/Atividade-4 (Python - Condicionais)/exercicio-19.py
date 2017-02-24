# -*- coding : utf-8 -*-

# Retornar mensagem de acordo com cores de trânsito

def mostra_mensagem(cor):
	if cor == 'V':
		return 'Siga'
	elif cor == 'A':
		return 'Atenção'
	else:
		return 'Pare'

assert mostra_mensagem('V') == 'Siga'
assert mostra_mensagem('A') == 'Atenção'
assert mostra_mensagem('E') == 'Pare'
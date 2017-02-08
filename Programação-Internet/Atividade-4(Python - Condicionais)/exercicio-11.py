# -*- coding : utf-8 -*-

# Mensagem se está febril ou não

VALOR_BASE = 35.6

def isFebril(temperatura):
	if temperatura > VALOR_BASE:
		return True
	return False

def mostrar_mensagem(temperatura):
	if isFebril(temperatura):
		return 'Está com febre'
	return 'Sem febre'

assert mostrar_mensagem(20) == 'Sem febre'
assert mostrar_mensagem(35) == 'Sem febre'
assert mostrar_mensagem(40) == 'Está com febre'
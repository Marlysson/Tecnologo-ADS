# -*- coding : utf-8 -*-

# Decidir se vai ficar em casa ou sair.

def ficar_em_casa_ou_sair(valor):
	if valor > 20:
		return "Vá ao cinema."
	return "Fique em casa."

assert ficar_em_casa_ou_sair(20) == 'Fique em casa.'
assert ficar_em_casa_ou_sair(25) == 'Vá ao cinema.'
assert ficar_em_casa_ou_sair(15) == 'Fique em casa.'
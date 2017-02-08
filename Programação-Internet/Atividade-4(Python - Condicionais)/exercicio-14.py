# -*- coding : utf-8 -*-

# Verificar se é maior de idade para votar para prefeito

def podeVotar(ano_nascimento):
	from datetime import date

	ano_atual = date.today().year

	if (ano_atual - ano_nascimento) >= 18:
		return True
	return False

assert podeVotar(1996) == True
assert podeVotar(1990) == True
assert podeVotar(2000) == False


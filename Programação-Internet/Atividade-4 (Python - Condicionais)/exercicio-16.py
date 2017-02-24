# -*- coding : utf-8 -*-

# Retornar o nome do mês baseado em um número

MESES = {
	1: 'Janeiro', 
	2: 'Fevereiro',
	3: 'Março',
	4: 'Abril',
	5: 'Maio',
	6: 'Junho',
	7: 'Julho',
	8: 'Agosto',
	9: 'Setembro',
	10: 'Outubro',
	11: 'Novembro',
	12: 'Dezembro'
}

def isMesValido(numero):
	if 1 <= numero <= 12:
		return True
	return False

def mostra_mensagem(numero_mes):
	if not isMesValido(numero_mes):
		return 'Mês inválido'
	else:
		'''
		if numero_mes == 1:
			return 'Janeiro'
		elif numero_mes == 2:
			return 'Fevereiro
		elif numero_mes == 3:
			return 'Março'
		...

		'''
		
		return MESES[numero_mes]

assert mostra_mensagem(1) == 'Janeiro'
assert mostra_mensagem(2) == 'Fevereiro'
assert mostra_mensagem(3) == 'Março'


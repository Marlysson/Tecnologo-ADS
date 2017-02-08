# -*- coding : utf-8 -*-

# Definir saudação de acordo com o sexo da pessoa.

def obter_saudacao(sexo):
	if sexo == 'masc':
		return 'llmo Sr.'
	return 'llma Sra.'

def obter_dados(nome,sexo):
	saudacao = obter_saudacao(sexo.lower())

	return '{} {}'.format(saudacao,nome)

assert obter_dados('Marlysson','masc') == 'llmo Sr. Marlysson'
assert obter_dados('Maria','fem') == 'llma Sra. Maria'
assert obter_dados('Marcelo','masc') == 'llmo Sr. Marcelo'
# -*- coding:utf8 -*-

dados_alunos = open('db_alunos.txt')

def converte_to_lista(dado):
	dados_alunos = []

	for i in dado:
		i = i.strip('\n')
		dados_alunos.append(i)
	return dados_alunos

def has_duplicates(arquivo):
	dados_alunos, nomes  = converte_to_lista(arquivo), []

	for aluno in dados_alunos:
		dados = aluno.split(';')
		nomes.append(dados[1])

	print nomes

	for nome in nomes:
		if nomes.count(nome) > 1:
			return True
	return False

def porcentagem(arquivo,s=None):
	generos = {'M':0,'F':0}

	dados_alunos = converte_to_lista(arquivo)

	for i in dados_alunos:
		dado = i.split(';')
		sexo = dado[3].upper()

		if sexo == 'M':
			generos['M'] += 1
		else:
			generos['F'] += 1

	total = generos['M'] + generos['F']

	porcent_masc = ( generos['M'] / float(total) ) * 100
	# porcent_fem  = ( generos['F'] / float(total) ) * 100
	porcent_fem = 100 - porcent_masc

	return {'masc':porcent_masc,'fem':porcent_fem}

dados = porcentagem(dados_alunos)
masc = dados['masc']
fem  = dados['fem']


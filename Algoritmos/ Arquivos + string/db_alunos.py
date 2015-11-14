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

	for nome in nomes:
		if nomes.count(nome) > 1:
			return True
	return False

def porcentagem(arquivo):
	masculino , feminino = 0 , 0

	dados_alunos = converte_to_lista(arquivo)

	for i in dados_alunos:
		dado = i.split(';')
		sexo = dado[3]

		if sexo == 'M':
			masculino += 1
		else:
			feminino += 1

	total = masculino + feminino

	porcent_masc = ( masculino / float(total) )* 100
	porcent_fem  = ( feminino / float(total) ) * 100

	return 'Masculino: {:.2f} %  \nFeminino: {:.2f} %'.format(porcent_masc, porcent_fem)

print porcentagem(dados_alunos)

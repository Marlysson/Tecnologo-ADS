# -*- coding:utf-8 -*-

def load_data(arquivo):
	'''Recupera os dados para serem usados no programa'''

	dados = open(arquivo)

	familias = []
	
	for familia in dados:
		data = familia.split("|")

		cod = data[0]
		membros = data[1]
		estado = data[2]
		cidade = data[3]
		renda = data[4].strip()

		f = [cod,membros,estado,cidade,renda]
		familias.append(f)

	return familias

def format_data(familia):
	'''Formata os dados inline para serem gravados'''
	nomes = familia[1].split(',')
	n = []

	for nome in nomes:
		n.append(nome.capitalize())
	nomes = ",".join(n)
	
	familia[1] = ",".join(n)
	familia = "|".join(familia)

	return familia






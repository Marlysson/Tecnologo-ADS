# -*- coding:utf-8 -*-

from operacoes import *
from dados import *
from random import randint

arquivo = 'bolsa_familia.txt'

funcionalidades = [
		'Inserir Família',
		'Quantidade Famílias por Estado',
		'Alterar Dados',
		'Calcular Benefício',
		'Sair'
]

def menu(opcoes):
	for opcao,valor in enumerate(opcoes):
		print '{} - {}'.format(opcao+1,valor)


while True:
	menu(funcionalidades)
	op = int(raw_input('Opção: '))

	if op == 1:
		quant_membros = int(raw_input('Digite a quantidade de membros: '))

		membros = []

		for i in range(quant_membros):
			membro = raw_input('Nome: ')
			membros.append(membro)		
		
		cod = "".join([
			str(randint(1,5)),
			str(randint(1,5)),
			str(randint(1,5))
		])

		membros = ",".join(membros)
		estado = raw_input('Estado: ').upper()
		cidade = raw_input('Cidade: ').capitalize()
		renda  = str(float(raw_input('Renda Total: ')))

		familia = format_data([cod,membros,estado,cidade,renda])
		if insert_family(familia,arquivo):
			print '\nInserido com sucesso'
		
	if op == 2:
		familias = load_data(arquivo)
		uf = raw_input('Digite o estado: ')

		familias = busca_by(familias,uf=uf)
		print len(familias)
		
		print '{}{}{}{}'.format('Código','Membros','Estado','Cidade','Renda')
		for f in familias:
			print '{:^10}{:^10}{:^10}{:^10}'.format(f[0].f[1],f[2],f[3],f[4])
		

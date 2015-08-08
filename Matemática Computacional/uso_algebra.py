# -*- coding:utf-8 -*-

from AlgebraLinear import Algebra

algebra = Algebra()

def menu():
		operacoes = [
			'Soma de Vetores',
			'Produto por escalar',
			'Produto Escalar',
			'Ângulo entre vetores',
			'Magnitude',
			'Normalização',
			'Inversão'
		]

		for opcao,operacao in enumerate(operacoes,start=1):
			print '{} - {}'.format(opcao,operacao)


continuar = 's'

while continuar == 's':

	menu()

	opcao = input('\nEscolha a operação: ')
	opcoes = [1,2,3,4,5,6,7]

	while opcao not in opcoes:
		print '\nDigite uma opção válida.'
		opcao = input('Escolha a operação: ')


	#CONJUNTO DE OPERAÇÕES

	if opcao == 1:
		
		vetor1 = input('Vetor 1: ')
		while not algebra.valida_vetor(vetor1):
			vetor1 = input('Digite um vetor válido: ')

		vetor2 = input('Vetor 2: ')

		while not algebra.valida_vetor(vetor2) or ( len(vetor2) != len(vetor1) ):
			print '\nVetor 2 deve ter {} elementos e serem válidos'.format(len(vetor1))
			vetor2 = input('Digite um vetor válido: ')

		soma_vetores = algebra.somar_vetores(vetor1,vetor2)
		print 'Soma dos vetores: {}'.format(soma_vetores)

		continuar = raw_input('\nDeseja Continuar? S/N ').lower()

	elif opcao == 2:

		escalar = input('Valor escalar: ')
		while not algebra.valida_escalar(escalar):
			escalar = input('Digite um escalar válido: ')

		vetor   = input('Vetor: ')
		while not algebra.valida_vetor(vetor):
			vetor   = input('Digite um vetor válido: ')

		produto_por_escalar = algebra.produto_por_escalar(escalar,vetor)
		print 'Vetor Resultante: {}'.format(produto_por_escalar)

		continuar = raw_input('\nDeseja Continuar? S/N ').lower()

	elif opcao == 3:

		vetor1 = input('Vetor 1: ')
		while not algebra.valida_vetor(vetor1):
			vetor1 = input('Digite um vetor válido: ')

		vetor2 = input('Vetor 2: ')

		while not algebra.valida_vetor(vetor2) or ( len(vetor2) != len(vetor1) ):
			print '\nVetor 2 deve ter {} elementos e serem válidos'.format(len(vetor1))
			vetor2 = input('Digite um vetor válido: ')

		produto_escalar = algebra.produto_escalar(vetor1,vetor2)
		print 'Produto escalar: {}'.format(produto_escalar)

		continuar = raw_input('\nDeseja Continuar? S/N ').lower()

	elif opcao == 4:
		
		vetor1 = input('Vetor 1: ')
		while not algebra.valida_vetor(vetor1):
			vetor1 = input('Digite um vetor válido: ')

		vetor2 = input('Vetor 2: ')
		while not algebra.valida_vetor(vetor2) or ( len(vetor2) != len(vetor1) ):
			print '\nVetor deve ter {} elementos e serem válidos'.format(len(vetor1))
			vetor2 = input('Digite um vetor válido: ')
		
		angulo_vetores = algebra.angulo(vetor1,vetor2)
		print '\nÂngulo entre vetores: {:.1f} graus'.format(angulo_vetores)

		continuar = raw_input('\nDeseja Continuar? S/N ').lower()

	elif opcao == 5:
		vetor = input('Vetor: ')

		while not algebra.valida_vetor(vetor):
			vetor   = input('Digite um vetor válido: ')

		magnitude = algebra.magnitude(vetor)
		print 'Magnitude do vetor: {:.2f}'.format(magnitude)

		continuar = raw_input('\nDeseja Continuar? S/N ').lower()

	elif opcao == 6:
		vetor = input('Vetor: ')
		while not algebra.valida_vetor(vetor):
			vetor = input('Digite um vetor válido: ')

		vetor_normalizado = [float(item) for item in algebra.normalizar(vetor)]

		print 'Vetor Normalizado : {}'.format(vetor_normalizado)

		continuar = raw_input('\nDeseja Continuar? S/N ').lower()

	elif opcao == 7:
		vetor = input('Vetor: ')

		while not algebra.valida_vetor(vetor):
			vetor   = input('Digite um vetor válido: ')

		vetor_invertido = algebra.inverter(vetor)
		print 'Vetor Inverso: {}'.format(vetor_invertido)
	
		continuar = raw_input('\nDeseja Continuar? S/N ').lower()
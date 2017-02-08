# -*- coding : utf-8 -*-

from is_multiplo import is_multiplo

'''
A partir de dois números fornecidos pelo usuário, escreva uma das seguintes mensagens:
	- Os dois são pares
	- Os dois são impares
	- O primeiro é par e o segundo é ímpar
	- O primeiro é ímpar e o segundo é par
'''

def mostra_mensagem(num1,num2):
	if is_multiplo(num1,2) and is_multiplo(num2,2):
		return 'Os dois são pares.'
	elif not is_multiplo(num1,2) and not is_multiplo(num2,2):
		return 'Os dois são ímpares.'
	elif is_multiplo(num1,2) and not is_multiplo(num2,2):
		return 'O primeiro é par e o segundo é ímpar.'
	elif not is_multiplo(num1,2) and is_multiplo(num2,2):
		return 'O primeiro é ímpar e o segundo é par.'

assert mostra_mensagem(10,12) == 'Os dois são pares.'
assert mostra_mensagem(11,11) == 'Os dois são ímpares.'
assert mostra_mensagem(10,11) == 'O primeiro é par e o segundo é ímpar.'
assert mostra_mensagem(11,12) == 'O primeiro é ímpar e o segundo é par.'
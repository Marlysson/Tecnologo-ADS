# -*- coding:utf8 -*-

numeros = [int(i) for i in raw_input('3 números: ').split()]

num1,num2,num3 = numeros

def maior(a,b):
	return (a + b + abs(a - b)) / 2

#pega o maior entre os dois primeiros
num_maior = maior(num1,num2)

#mostra direto comparando com o terceiro número
print 'O maior é : {}'.format(maior(num_maior,num3))
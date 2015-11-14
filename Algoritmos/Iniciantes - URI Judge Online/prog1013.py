# -*- coding:utf8 -*-

def maior(a,b):
	return (a + b + abs(a - b)) / 2

num1,num2,num3 = [int(i) for i in raw_input().split()]

#pega o maior entre os dois primeiros
num_maior = maior(num1,num2)

#mostra direto comparando com o terceiro número
print '{} eh o maior'.format(maior(num_maior,num3))
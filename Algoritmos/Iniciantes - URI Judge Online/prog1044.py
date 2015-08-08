# -*- coding:utf8 -*-

numeros = raw_input('Digite 2 números: ').split()
A,B = [int(i) for i in numeros]

if A % B == 0 or B % A == 0:
	print 'São múltiplos'
else:
	print 'Não são múltiplos'

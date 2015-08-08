# -*- coding:utf8 -*-

lados = raw_input('Lados do Triângulo: ').split()

A,B,C = [float(i) for i in lados]

if abs(A - B) < C  and C < (A + B):
	print 'FORMA UM TRIÂNGULO'
	print 'PERÍMETRO: {}'.format(A+B+C)
else:
	area = ( C * (A + B) ) / 2
	print 'NÃO FORMA UM TRIÂNGULO'
	print 'ÁREA : {}'.format(area)

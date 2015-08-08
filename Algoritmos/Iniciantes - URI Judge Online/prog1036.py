# -*- coding:utf-8 -*-
from math import sqrt

valores = raw_input('3 valores separados por espaço: ').split()
valor_a,valor_b,valor_c = [float(i) for i in valores]

delta = pow(valor_b,2) - (4 * valor_a * valor_c)

if delta < 0 or valor_a == 0:
	print 'Impossível Calcular'
else:
	delta = sqrt(delta)
	raiz_um = (-valor_b + delta) / (2 * valor_a)
	raiz_dois = (-valor_b - delta) / (2 * valor_a)

	print 'Raiz 1 é: %.5f' %raiz_um
	print 'Raiz 2 é: %.5f' %raiz_dois
 
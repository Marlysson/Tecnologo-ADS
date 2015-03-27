# -*- coding :utf-8 -*-

x = float(input('Valor do eixo X: '))
y = float(input('Valor do eixo Y: '))

if x == 0 and y == 0:
	print 'Origem'
elif x == 0:
	print 'Eixo Y'
elif y == 0:
	print 'Eixo X'
else:
	if x > 0 and y > 0:
		print 'Quadrante 1'
	elif x < 0 and y > 0:
		print 'Quadrante 2'
	elif x < 0 and y < 0:
		print 'Quadrante 3'
	elif x > 0 and y < 0:
		print 'Quadrante 4'


'''
Quadrantes

     	-/+ |  +/+
     _______|_______
     		|
        -/- |  +/-
'''


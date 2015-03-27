# -*- coding:utf-8 -*-
numero = float(input('Número entre 0 e 100: '))

while numero < 0 or numero > 100:
	print 'Valor fora do Intervalo'
	numero = input('Digite um número: ')

if 0 <= numero <= 25:
	print 'Intervalo [0,25]'
elif 25 < numero <= 50:
	print 'Intervalo [25,50]'
elif 50 > numero <= 75:
	print 'Intervalo [50,75]'
elif 75 < numero <= 100:
	print 'Intervalo [75,100]'


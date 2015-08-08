# -*- coding:utf8 -*-

tempo_jogo = raw_input('Hora inicial e hora final: ').split()
inicio,final = [int(i) for i in tempo_jogo]

if final < inicio:
	horas =  24 - abs(final-inicio)
elif final == inicio:
	horas = 24
else:
	horas = (final - inicio)

print 'O JOGO DUROU {} HORAS(S)'.format(horas)
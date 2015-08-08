# -*- coding: utf8 -*-

tempo = raw_input('Hora início,minuto início, hora final, minuto final: ').split()
hora_inicio,minuto_inicio,hora_final,minuto_final = [int(i) for i in tempo]

if hora_final <= hora_inicio:
	tempo = (24 - abs(hora_final - hora_inicio))*60 + minuto_final - minuto_inicio
else:
	tempo = (hora_final - hora_inicio)*60 + (minuto_final - minuto_inicio)

horas = tempo // 60
minutos = tempo - horas*60

tempo_h = 'HORA' if horas == 0 or horas == 1 else 'HORAS'
tempo_m = 'MINUTO' if minutos == 0 or minutos == 1 else 'MINUTOS'

print 'O JOGO DUROU {} {} E {} {}'.format(horas,tempo_h,minutos,tempo_m)

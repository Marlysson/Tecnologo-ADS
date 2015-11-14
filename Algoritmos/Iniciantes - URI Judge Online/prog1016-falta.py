# -*- coding:utf-8 -*-

distancia = int(input('Distância: '))

def funcao_horaria(inicio,vel):
	return inicio + vel * tempo

carro1 = funcao_horaria()
# tempo = int(distancia / float(90 - 60) * 60)

print 'Tempo para alcançar: {} minuto(s)'.format(tempo)
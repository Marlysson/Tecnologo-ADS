# -*- coding:utf-8 -*-

distancia = int(input('Distância: '))

# veloc.média com a diferença da velocidade entre os carros
tempo = int(distancia / float(90 - 60) * 60)

print 'Tempo para alcançar: {} minuto(s)'.format(tempo)
# -*- coding : utf-8 -*-

# Distância media da viagem : km/h

def velocidade_media(distancia,tempo):
	return distancia / float(tempo)

assert velocidade_media(100,1) == 100.0
assert velocidade_media(200,2) == 100.0
assert velocidade_media(300,3) == 100.0

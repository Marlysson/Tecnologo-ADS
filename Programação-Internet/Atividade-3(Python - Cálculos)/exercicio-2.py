# -*- coding : utf-8 -*-

def obter_horas(minutos):
	return minutos // 60

def obter_minutos(minutos):
	return minutos % 60

minutos = 144

horas_totais = obter_horas(minutos)
minutos_totais = obter_minutos(minutos)

print("Minutos totais: {}".format(minutos))
print("Horas: {}".format(horas_totais))
print("Minutos: {}".format(minutos_totais))

# -*- coding : utf-8 -*-

def to_unidade_dezena_centena(valor):

	centena = valor // 100
	dezena = ( valor - centena * 100) // 10
	unidade = valor - (centena * 100 + dezena * 10)

	resultado = str(unidade)+str(dezena)+str(centena)

	return resultado

print(to_unidade_dezena_centena(435))

# -*- coding:utf8 -*-

def prim_ult(palavra,num):
	primeiros = palavra[:num]
	ultimos   = palavra[len(palavra)-num:]

	retorno = 'Primeiros: {} \nUltimos: {}'.format(primeiros,ultimos)

	return retorno

print prim_ult('Instituto',2)
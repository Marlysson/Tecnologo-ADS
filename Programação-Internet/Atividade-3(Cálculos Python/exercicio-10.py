# -*- coding : utf-8 -*-

def media_ponderada(numbers,pesos):
	
	values  = list(zip(numbers,pesos))

	soma = 0

	for valor , peso in values:
		soma += valor * peso

	return soma / sum(pesos)

print(media_ponderada(numbers=[1,2,3,4],pesos=[1,2,3,4]))
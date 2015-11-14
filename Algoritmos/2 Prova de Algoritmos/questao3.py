#-*- coding: utf-8 -*-

'''
[TEORIA]
	O algoritmo percorre toda a lista que contém os números,
	e dependendo da condição (crescente,decrescente) ela faz
	ou não a troca do elemento posterior com o elemento atual até
	que todos os elementos da lista estejam ordenados na ordem desejada.
'''
import random
numeros = random.sample(range(1,100),10)

def bubble_sort(lista):
	for i in range(len(lista)):
		for n in range(len(lista) - 1):
			if lista[n+1] < lista[n]:
				aux = lista[n]
				lista[n] = lista[n+1]
				lista[n+1] = aux
	return lista


print "\nLista original: {}".format(numeros)
print "Lista ordenada: {}\n".format(bubble_sort(numeros))

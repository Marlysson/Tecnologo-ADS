# -*- coding:utf8 -*-

def bubble_sort(lista):
	for i in range(len(lista)-1):
		for i in range(len(lista)-1):
			if lista[i] > lista[i+1]:
				aux = lista[i]
				lista[i] = lista[i+1]
				lista[i+1] = aux

	return lista


from random import sample

lista = sample(xrange(100),10)

print bubble_sort(lista)

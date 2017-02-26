# -*- coding: utf-8 -*-

'''
Criar um algoritmo que leia um número que será o limite superior de um intervalo
 e o incremento (inc). Imprimir todos os números naturais 
 no intervalo de zero até o limite superior. 
 Suponha que o incremento é maior do que
zero e o limite superior maior que o incremento.
'''

limite = int(input("Limite superior: "))
incremento = int(input("Incremento: "))

for i in range(1,limite,incremento):
	print(i)

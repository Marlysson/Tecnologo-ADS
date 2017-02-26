# -*- coding: utf-8 -*-

'''
Sabendo-se que a UAL calcula o produto através de somas sucessivas, 
criar um algoritmo que calcule o produto
de dois números inteiros lidos. 
Suponha que os números lidos sejam positivos e que o multiplicando seja menor
do que o multiplicador.
'''

def somar(num1,num2):
	return num1 + num2

n1 = 11
n2 = 7
soma = 0

for _ in range(1,n2+1):
	soma += somar(n1,0)

print("Multiplicação entre %d e %d é : %d" %(n1,n2,soma))

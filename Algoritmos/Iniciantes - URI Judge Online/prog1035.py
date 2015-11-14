# -*- coding:utf-8 -*-
'''
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior 
do que C e se D for maior do que A e a soma de C com D for maior
que a soma de A e B e se C e D, ambos,forem positivos e se a 
variável A for par escrever a mensagem "Valores aceitos",
senão escrever "Valores nao aceitos".
'''

numeros = raw_input('4 números separados por espaço: ').split()

A,B,C,D = int(numeros[0]),int(numeros[1]),int(numeros[2]),int(numeros[3])
# A,B,C,D = [int(i) for i in numeros]

if (B > C and D > A) and (C+D > A+B) and (C > 0 and D > 0) and (A%2==0):
	print 'Valores aceitos'
else:
	print 'Valores nao aceitos'

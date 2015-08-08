# -*- coding:utf-8 -*-

num1 = input('Primeiro número: ')
num2 = input('Segundo número: ')
som_impares = 0

if num1 >= num2:
	maior = num1
	menor = num2
else:
	maior = num2
	menor = num1

atual = menor+1

while atual != maior:
	if atual % 2 == 1:
		som_impares += atual
	atual +=1

print som_impares
	
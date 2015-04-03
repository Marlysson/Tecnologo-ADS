# -*- coding:utf8 -*-

lados = [float(i) for i in raw_input('Lados do triângulo: ').split()]
lados.sort(reverse=True) #ordem decrescente

A,B,C = lados

#Classificação dos ângulos
if A >= B + C:
	print 'NÃO FORMA TRIÂNGULO'
elif pow(A,2) == pow(B,2) + pow(C,2):
	print 'TRIÂNGULO RETÂNGULO'
elif pow(A,2) > pow(B,2) + pow(C,2):
	print 'TRIÂNGULO OBTUSÂNGULO'
elif pow(A,2) < pow(B,2) + pow(C,2):
	print 'TRIÂNGULO ACUTÂNGULO'

#Classificação dos lados
if A == B == C:
	print 'TRIÂNGULO EQUILÁTERO'
elif A == B or A == C or B == C:
	print 'TRIÂNGULO ISÓCELES'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
# -*- coding:utf8 -*-

def char_repeated(palavra):
	caracteres = ''
	for i in palavra:
		if palavra.count(i) >= 2 and i not in caracteres:
			caracteres += i
	return caracteres

print 'Letras repetidas: {}'.format(char_repeated('paralelepipedo'))
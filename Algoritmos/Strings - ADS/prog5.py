# -*- coding:utf8 -*-

def replace_repeated(palavra):
	palavra = palavra.lower()
	for i in palavra:
		if palavra.count(i) >= 2:
			palavra = palavra.replace(i,'')
	return palavra

print replace_repeated('paralelepipedo')

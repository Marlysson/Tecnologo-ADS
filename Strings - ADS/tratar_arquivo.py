# -*- coding:utf8 -*- 

palavras = open('palavras-portugues.txt')

def mais_vinte_caracteres(arquivo):

	words = []
	for i in arquivo:
		i = i.strip()
		if len(i) > 20:
			words.append(i)
	return words

def has_no_e(palavra):
	if 'e' in palavra:
		return False
	return True

def palavra_sem_e():
	palavras_sem_e = []
	cont = 0.0

	for i in arquivo:
		cont += 1
		i = i.strip()
		if 'E' not in i:
			palavras_sem_e.append(i)

	print 'Palavras sem a letra \'e\''	
	for i in palavras_sem_e:
		print i

	porcentagem = (len(palavras_sem_e) / cont ) * 100.0
	print 'Porcentagem de palavras sem \'e\': {:.2f} % '.format(porcentagem)

def avoids(palavra,letras):
	for i in letras:
		if i in palavra:
			return False
		return True








		


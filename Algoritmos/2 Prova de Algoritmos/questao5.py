#-*- coding: utf-8 -*-
import os

palavras = os.path.join("arquivos","palavras.txt")

palavras = [palavra.strip() for palavra in open(palavras)]

reverses = {}

for i in range(len(palavras)):
	cont = 0
	palavra = palavras[i]

	chaves = reverses.keys()
	valores = reverses.values()
	
	if (palavra not in valores) and (palavra not in chaves):
		while cont != len(palavras):
			if palavra == palavras[cont][::-1]: # atalho do python para inverter string
				reverses[palavra] = palavras[cont]
			cont += 1

print "\n{:^15}{:^20}".format("Palavra","Reverse Pair")
print "------------------------------------"
for palavra in reverses:
	print "{:^15}{:^20}".format(palavra,reverses[palavra])
	print "------------------------------------"


#-*- coding: utf-8 -*-
import os
alunos = []

gabarito = os.path.join("arquivos","gabarito.txt")
cartoes  = os.path.join("arquivos","cartoes.txt")

for i in open(gabarito):
	gabarito = list(str(i).upper())


for dados_aluno in open(cartoes):
	aluno = dados_aluno.strip().split("#")
	matric , prova = aluno[0] , list(str(aluno[1]).upper())
	nota = 0

	for pos in range(len(gabarito)):
		if gabarito[pos] == prova[pos]:
			nota += 1
	alunos.append((matric,prova,float(nota)))


print "\n{:^15}{:^20}".format("Matrícula","Nota")
print "------------------------------------"
for matricula,respostas,nota in alunos:
	print "{:^15}{:^20}".format(matricula,nota)
	print "------------------------------------"
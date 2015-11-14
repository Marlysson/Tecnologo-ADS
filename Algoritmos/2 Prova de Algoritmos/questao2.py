#-*- coding: utf-8 -*-

alunos = []

for i in open("gabarito.txt"):
	gabarito = list(str(i).upper())


for dados_aluno in open("cartoes.txt"):
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
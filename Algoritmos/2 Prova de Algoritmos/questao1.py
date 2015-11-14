#-*- coding: utf-8 -*-

quant_alunos = int(raw_input('Quantidade de alunos: '))
notas = raw_input('Notas: ').split()
# notas = [20,25,85,40,25,90,25,40,55,40]

frequencias = {}
notas_maiores = []

for nota in notas:
	if nota not in frequencias:
		frequencias[nota] = 1
	else:
		frequencias[nota] += 1

max_frequencia = max(frequencias.values())

for nota in frequencias:
	if frequencias[nota] == max_frequencia:
		notas_maiores.append(nota)

print "Nota mais frequente: {}".format(max(notas_maiores))




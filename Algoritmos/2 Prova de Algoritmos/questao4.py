#-*- coding: utf-8 -*-

nomes = [nome.strip() for nome in open("nomes.txt")]
dados = []

def remove_all(lista,item):
	count = lista.count(item) -1
	for i in range(count):
		lista.remove(item)

for nome in nomes:
	quantidade_nome = nomes.count(nome)

	if quantidade_nome >= 2:
		dados.append([nome,quantidade_nome])
		remove_all(nomes,nome)


def ordena_quant(x,y):
	return cmp(x[1],y[1])

dados.sort(cmp=ordena_quant,reverse=True)

print "\n{:^15}{:^20}".format("Nome","Quantidade")
print "------------------------------------"
for nome,quantidade in dados:
	print "{:^15}{:^20}".format(nome,quantidade)
	print "------------------------------------"

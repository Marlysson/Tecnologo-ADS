# -*- coding : utf-8 -*-

moedas = {
	0.01:0,
	1:0,
	5:0,
	10:0,
	25:0,
}

for moeda in [0.01,1,5,10,25]:
	if moeda == 0.01:
		quantidade = int(input("Quantidade de moedas de : {moeda} centavo(s): ".format(moeda=moeda)))
	else:
		quantidade = int(input("Quantidade d moedas de : {moeda} real(s): ".format(moeda=moeda)))

	moedas[moeda] = quantidade

resultado = 0

for moeda,quantidade in moedas.items():
	resultado += moeda * quantidade

print("Você já possui: R$ {:.2f}".format(resultado))
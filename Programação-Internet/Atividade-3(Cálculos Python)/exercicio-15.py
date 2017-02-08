# -*- coding : utf-8 -*-


def descontar(valor_total,percentual_desconto):
	return valor_total - (valor_total * percentual_desconto)

print("Valor : 10")
print("Percentual: 10%")
print("Novo valor: R$ {}".format(descontar(valor_total=10,percentual_desconto=0.1)))
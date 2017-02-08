# -*- coding : utf-8 -*-

cedulas = [50,10,5,1]

def troco(valor):
		
	# cedula_50 = valor // 50
	# cedula_10 = (valor - cedula_50 * 50) // 10
	# cedula_5  = (valor - cedula_50 * 50 - cedula_10 * 10) // 5
	# cedula_1 = valor - cedula_50 * 50 - cedula_10 * 10 - cedula_5 * 5

	cedula_50 = valor // 50
	valor = valor % 50

	cedula_10 = valor // 10
	valor = valor % 10

	cedula_5 = valor // 5
	valor = valor % 5

	cedula_1 = valor // 1

	return {"50":cedula_50,"10":cedula_10,"5":cedula_5,"1":cedula_1}

valor = int(input("Digite o troco: "))

resultado = troco(valor)

for cedula in cedulas:
	print("{} cédula(s) de {}".format(resultado[str(cedula)],cedula))
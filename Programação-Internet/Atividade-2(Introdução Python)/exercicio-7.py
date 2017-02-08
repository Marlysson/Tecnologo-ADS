# -*- coding : utf-8 -*-

to_litros = lambda miligramas : miligramas / 1000

lata = 350
garrafa_1 = 600
garrafa_2 = 2000

quant_lata = int(input("Quantidade de latas(350ml): "))
quant_garrafa_1 = int(input("Quantidade de garrafas(600ml): "))
quant_garrafa_2 = int(input("Quantidade de garrafas(2L): "))


total_litros = quant_lata * lata + \
			   quant_garrafa_1 * garrafa_1 + \
			   quant_garrafa_2 * garrafa_2

print("Quantidade de litros : {}".format(to_litros(total_litros)))
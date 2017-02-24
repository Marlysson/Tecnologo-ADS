# -*- coding : utf-8 -*-

to_quilo = lambda gramas : gramas / 1000

quant_queijo_total = 50
quant_presunto_total = 50
quant_hamburger_total = 100

quant_sanduiche = int(input("Quantidade de sanduíches : "))

total_queijo = quant_queijo_total * quant_sanduiche
total_presunto = quant_presunto_total * quant_sanduiche
total_hamburger = quant_hamburger_total * quant_sanduiche

print("Quantidade de queijo: {} quilo(s)".format(to_quilo(total_queijo)))
print("Quantidade de presunto: {} quilo(s)".format(to_quilo(total_presunto)))
print("Quantidade de hamburger: {} quilo(s)".format(to_quilo(total_hamburger)))
# -*- coding : utf-8 -*-

preco_pequena = 10
preco_medio   = 12
preco_grande  = 15

quant_pequena = int(input("Quantidade de camisas pequenas: "))
quant_media   = int(input("Quantidade de camisas médias: "))
quant_grande   = int(input("Quantidade de camisas grandes: "))

total_arrecadado = quant_pequena * preco_pequena + quant_media * preco_medio + quant_grande * preco_grande

print("Total arrecadado : R$ {:.2f}".format(total_arrecadado))
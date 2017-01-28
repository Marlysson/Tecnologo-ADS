# -*- coding : utf-8 -*-

custo_anel_com_chip = 4
custo_anel_alimento = 3.5 * 2

quant_frangos = int(input("Quantidade de frangos: "))

custo_total = custo_anel_alimento * quant_frangos + custo_anel_com_chip * quant_frangos

print("Gasto total : R$ {:.2f}".format(custo_total))
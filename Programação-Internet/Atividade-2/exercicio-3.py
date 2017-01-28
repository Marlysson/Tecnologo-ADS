# -*- coding : utf-8 -*-

valor_conta = float(input("Valor da conta: "))

carlos = andre = felipe = valor_conta / 3

diferenca = lambda valor : valor - int(valor)

diferenca_carlos = diferenca(carlos)
diferenca_andre  = diferenca(andre)

felipe += diferenca_andre + diferenca_carlos

print("Carlos deve pagar: R$ {:.2f}".format(carlos - diferenca_carlos))
print("André deve pagar: R$ {:.2f}".format(andre - diferenca_andre))
print("Felipe deve pagar: R$ {:.2f}".format(felipe))
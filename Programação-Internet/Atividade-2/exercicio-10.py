# -*- coding : utf-8 -*-

salario = 1200
c1 = 200
c2 = 120

dois_por_cento = lambda valor : valor * 0.02

acrescimo = c1 + dois_por_cento(c1) + c2 + dois_por_cento(c2)
restante = salario - acrescimo

print("Terá de pagar : R$ {:.2f}".format(acrescimo))
print("E restará R$ {:.2f}".format(restante))
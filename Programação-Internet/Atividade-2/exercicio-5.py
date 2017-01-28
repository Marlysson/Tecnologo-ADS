# -*- coding : utf-8 -*-

horas_trabalhadas = int(input("Quantidade de horas trabalhadas: "))

if horas_trabalhadas > 8:
	horas_extras = horas_trabalhadas - 8
	horas_normais = horas_trabalhadas - horas_extras
else:
	horas_normais = horas_trabalhadas
	horas_extras = 0

salario_bruto = horas_normais * 10 + horas_extras * 15
salario_liquido = salario_bruto - ( salario_bruto * 0.1 )

print("Salário bruto: R$ {:.2f}".format(salario_bruto))
print("Salário líquido: R$ {:.2f}".format(salario_liquido))
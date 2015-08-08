# -*- coding:utf8 -*-

salario = float(input('Informe seu salário: '))

if 0 <= salario <= 400.00:
	reajuste = 0.15
	novo_salario = salario + (salario * reajuste)
elif 400.01 <= salario <= 800.00:
	reajuste = 0.12
	novo_salario = salario + (salario * reajuste)
elif 800.01 <= salario <= 1200.00:
	reajuste = 0.10
	novo_salario = salario + (salario * reajuste)
elif 1200.01 <= salario <= 2000.00:
	reajuste = 0.07
	novo_salario = salario + (salario * reajuste)
elif salario > 2000.00:
	reajuste = 0.04
	novo_salario = salario + (salario * reajuste)


print '\nNovo salário: R$ {:.2f}'.format(novo_salario)
print 'Reajuste ganho: R$ {:.2f}'.format(salario * reajuste)
print 'Em percentual : {}%'.format(int(reajuste*100))
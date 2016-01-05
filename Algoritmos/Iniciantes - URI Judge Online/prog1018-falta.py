# -*- coding:utf8 -*-
valor_total = input('Digite o valor que deseja: ')

# notas = {
# 	'100':0,
# 	'50':0,
# 	'20':0,
# 	'10':0,
# 	'5':0,
# 	'2':0,
# 	'1':0
# }

# while valor_total:
# 	if valor_total >= 100:
# 		notas['100'] += valor_total // 100
# 		valor_total %= notas['100'] * 100
# 	if valor_total >= 50:
# 		notas['50'] += valor_total // 50
# 		valor_total %= notas['50'] * 50
# 	if valor_total >= 20:
# 		notas['20'] += valor_total // 20
# 		valor_total %= notas['20'] * 20
# 	if valor_total >= 10:
# 		notas['10'] += valor_total // 10
# 		valor_total %= notas['10'] * 10
# 	if valor_total >= 5:
# 		notas['5'] += valor_total // 5
# 		valor_total %= notas['5'] * 5
# 	if valor_total >= 2:
# 		notas['2'] += valor_total // 2
# 		valor_total %= notas['2'] * 2
# 	if valor_total >= 1:
# 		notas['1'] += valor_total // 1
# 	break

# print '{} nota(s) de 100.'.format(notas['100'])
# print '{} nota(s) de 50.'.format(notas['50'])
# print '{} nota(s) de 20.'.format(notas['20'])
# print '{} nota(s) de 10.'.format(notas['10'])
# print '{} nota(s) de 5.'.format(notas['5'])
# print '{} nota(s) de 2.'.format(notas['2'])
# print '{} nota(s) de 1.'.format(notas['1'])

cedulas = [100,50,20,10,5,2,1]

for i in cedulas:
	valor = valor_total // i
	valor_total -= valor * i

	print "{} cédulas de R${:.2f}".format(valor,i)
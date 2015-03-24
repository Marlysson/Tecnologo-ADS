valor_total = input('Digite o valor que deseja: ')

notas_100,notas_50,notas_20,notas_10,notas_5,notas_2,notas_1 = 0,0,0,0,0,0,0

while valor_total:
	if valor_total >= 100:
		notas_100 += valor_total // 100
		valor_total %= notas_100 * 100
	if valor_total >= 50:
		notas_50 += valor_total // 50
		valor_total %= notas_50 * 50
	if valor_total >= 20:
		notas_20 += valor_total // 20
		valor_total %= notas_20 * 20
	if valor_total >= 10:
		notas_10 += valor_total // 10
		valor_total %= notas_10 * 10
	if valor_total >= 5:
		notas_5 += valor_total // 5
		valor_total %= notas_5 * 5
	if valor_total >= 2:
		notas_2 += valor_total // 2
		valor_total %= notas_2 * 2
	if valor_total >= 1:
		notas_1 += valor_total // 1
	break

print '{} nota(s) de 100.'.format(notas_100)
print '{} nota(s) de 50.'.format(notas_50)
print '{} nota(s) de 20.'.format(notas_20)
print '{} nota(s) de 10.'.format(notas_10)
print '{} nota(s) de 5.'.format(notas_5)
print '{} nota(s) de 2.'.format(notas_2)
print '{} nota(s) de 1.'.format(notas_1)

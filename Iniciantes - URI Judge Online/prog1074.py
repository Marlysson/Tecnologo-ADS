# -*- coding:utf8 -*-

testes = int(input('Quantidade de testes: '))

for i in range(testes):
	numero = int(input('Número: '))

	if numero == 0:
		print 'NULL'
	else:
		if numero % 2 == 0:
			print 'EVEN',
		else:
			print 'ODD',
			
		if numero > 0:
			print 'POSITIVE'
		else:
			print 'NEGATIVE'
		


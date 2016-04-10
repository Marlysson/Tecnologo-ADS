# -*- coding :utf8 -*-

testes = int(input('Quantidade de testes: '))
coelho,rato,sapo = 0 , 0 , 0

for i in range(testes):
	dados = raw_input('Tipo: ').split()
	quantidade, tipo  = int(dados[0]) , dados[1].upper()

	if tipo == 'C':
		coelho += quantidade
	elif tipo == 'R':
		rato += quantidade
	elif tipo == 'S':
		sapo += quantidade

total = coelho + rato + sapo

print '\nTotal: {}'.format(total)
print 'Total de coelhos: {}'.format(coelho)
print 'Total de ratos: {}'.format(rato)
print 'Total de sapos: {}'.format(sapo)
print 'Percentual de coelhos: {:.2%}'.format( coelho/float(total) )
print 'Percentual de ratos {:.2%}'.format( rato/float(total) )
print 'Percentual de sapos {:.2%}'.format( sapo/float(total) )

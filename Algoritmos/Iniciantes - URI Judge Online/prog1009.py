nome = raw_input('Nome do vendedor: ')
salario = float(input('Salario: '))
total_venda = float(input('Total de vendas: '))

total_mes = salario + ( total_venda*0.15 )
print 'TOTAL = R$ %.2f' %total_mes
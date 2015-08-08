num_funcionario = int(input('Numero do funcionario: '))
horas_trab      = int(input('Horas trabalhadas: '))
valor_horas     = float(input('Valor da hora: '))

salario = horas_trab * valor_horas
print 'NUMERO =',num_funcionario
print 'SALARIO = R$%.2f' % salario
num_funcionario = int(input('Numero do funcionario: '))
horas_trab      = int(input('Horas trabalhadas: '))
valor_horas     = float(input('Valor da hora: '))

salario = horas_trab * valor_horas
print 'NUMBER =',num_funcionario
print 'SALARY = U$ %.2f' % salario
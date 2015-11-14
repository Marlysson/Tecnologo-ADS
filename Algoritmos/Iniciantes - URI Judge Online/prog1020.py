# coding:utf-8
'''
	Leia um valor inteiro correspondente à idade de uma pessoa em dias 
	e informe-a em anos, meses e dias
'''

idade = int(input('Idade em dias: '))

ano = idade // 365
meses = ( idade - (ano*365) ) // 30
dias = idade - (ano*365) - (meses*30)


print '{} ano(s)'.format(ano)
print '{} mes(es)'.format(meses)
print '{} dias(s)'.format(dias)

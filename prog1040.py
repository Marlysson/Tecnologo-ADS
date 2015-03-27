# -*- coding:utf-8 -*-

nota_1 = float(input('Digite a nota 1: '))
nota_2 = float(input('Digite a nota 2: '))
nota_3 = float(input('Digite a nota 3: '))
nota_4 = float(input('Digite a nota 4: '))

media = (nota_1*2 + nota_2*3 + nota_3*4 + nota_4*1) / float(2+3+4+1)

print '\nMédia %.1f' % media

if media >= 7.0:
	print 'Aluno aprovado'
elif media < 5.0:
	print 'Aluno reprovado'
elif media >= 5.0 and media <= 6.9:
	print 'Aluno em exame'
	exame = float(input('Nota do Exame: '))
	media = ( exame + media ) / 2

	if media >= 5:
		print 'Aluno Aprovado'
	elif media <= 4.9:
		print '\nAluno Reprovado'
	print 'Média Final: %.1f' %media

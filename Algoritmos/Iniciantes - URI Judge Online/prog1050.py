# -*- coding:utf8 -*-

ddds = {
	61:'Brasília',
	71:'Salvador',
	11:'São Paulo',
	21:'Rio de Janeiro',
	32:'Juiz de Fora',
	19:'Campinas',
	27:'Vitória',
	31:'Belo Horizonte',
}

ddd = int(input('DDD do local: '))

if not ddds.has_key(ddd):
	print 'DDD não cadastrado'
else:
	print '\nLocal: {}'.format(ddds.get(ddd))


# -*- coding:utf-8 -*-

produtos = {
	'1':{'produto': 'cachorro_quente', 'valor': float(4)   },
	'2':{'produto': 'x-salada'       , 'valor': float(4.50)},
	'3':{'produto': 'x-bacon'        , 'valor': float(5)   },
	'4':{'produto': 'torrada_simples', 'valor': float(2)   },
	'5':{'produto': 'refrigerante'   , 'valor': float(1.50)}
}

codigo = str(input('Código do produto: '))
quantidade = int(input('Quantidade de: '))

print 'Quantidade a pagar: R$ %.2f' % (quantidade*produtos[codigo]['valor'])


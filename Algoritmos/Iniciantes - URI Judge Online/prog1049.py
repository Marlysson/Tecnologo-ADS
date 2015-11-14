# -*- coding:utf8 -*-

dados = {
	'vertebrado':{
		'ave':{
			'carnivoro':'aguia',
			'onivoro':'pomba'
		},
		'mamifero':{
			'onivoro':'homem',
			'herbivoro':'vaca'
		}
	},

	'invertebrado':{
		'inseto':{
			'hematofago':'pulga',
			'herbivoro':'lagarta'
		},
		'anelideo':{
			'hematofago':'sanguessuga',
			'onivoro':'minhoca'
		}
	}
}


palavra1 = raw_input('1 palavra para identificar: ')
palavra2 = raw_input('2 palavra para identificar: ')
palavra3 = raw_input('3 palavra para identificar: ')

print 'Animal escolhido : {}'.format(dados.get(palavra1).get(palavra2).get(palavra3))
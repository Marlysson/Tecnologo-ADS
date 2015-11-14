# -*- coding:utf-8 -*-

from dados import *

arquivo = 'bolsa_familia.txt'

def insert_family(family,arquivo):
	with open(arquivo) as dados:
		dados.write('\n'+family)
	return True

def busca_by(familias,cod=None,uf=None,city=None):

	if cod:
		familias = [f for f in familias if f[0] == cod]
	if uf:
		familias = [f for f in familias if f[2] == uf]
	if city:
		familias = [f for f in familias if f[3] == city]

	return familias

def alterar_dados(familia,atributo):
	pass

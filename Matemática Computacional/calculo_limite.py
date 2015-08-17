# -*- coding:utf8 -*-

def f(x):
	return x**2

def calc_delta(p1,p2):
    return abs(p1-p2)/2.0

def lim(ponto,precisao):
	delta = 1
	lim = ponto + calc_delta(ponto,ponto+delta)

	while abs(lim - ponto) >= precisao:
		lim = ponto + calc_delta(ponto,lim)
		delta = calc_delta(ponto,lim)
	return lim


precisao = float(input('Digite a precisão: '))
ponto = float(input('Digite um ponto para o limite: '))

print 'Limite de f({}) = {}'.format(ponto,lim(f(ponto),precisao))

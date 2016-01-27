# -*- coding: utf-8 -*-

class Vetor(object):
	def __init__(self,ponto_x,ponto_y):
		self.x = ponto_x
		self.y = ponto_y

	def __repr__(self):
		return 'Vetor({:.1f},{:.1f})'.format(self.x,self.y)


from math import sqrt

def distancia(x1,x2,y1,y2):

	distancia = sqrt( pow(( float(x2)-float(x1) ),2) + pow( ( float(y2)-float(y1) ),2) )
	return distancia

x1,y1 = raw_input('Dois valores do ponto 1: ').split()
x2,y2 = raw_input('Dois valores do ponto 2: ').split()

distancia = distancia(x1,x2,y1,y2)	

print 'DISTANCIA ENTRE OS PONTOS: %.4f' %distancia
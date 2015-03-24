from math import sqrt
ponto1 = raw_input('Dois valores do ponto 1: ')
ponto2 = raw_input('Dois valores do ponto 2: ')

x1,y1 = ponto1.split()
x2,y2 = ponto2.split()

distancia = sqrt( (int(x2) - int(x1))**2 + (int(y2) - int(y1))**2 )

print 'DISTANCIA ENTRE OS PONTOS %.2f ' %distancia
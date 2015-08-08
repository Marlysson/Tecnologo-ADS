valorA = float(input('Valor A: '))
valorB = float(input('Valor B: '))
valorC = float(input('Valor C: '))

pi = 3.14159
triangulo_retangulo = ( valorA * valorC ) / 2
circulo  			= pi * valorC**2
trapezio			= ( ( valorA + valorB ) * valorC ) / 2
quadrado			= valorB**2
retangulo 			= valorA * valorB

print 'TRIANGULO RETANGULO = %.3f' %triangulo_retangulo
print 'CIRCULO = %.3f' %circulo
print 'TRAPEZIO = %.3f' %trapezio
print 'QUADRADO  = %.3f' %quadrado
print 'RETANGULO  = %.3f' %retangulo

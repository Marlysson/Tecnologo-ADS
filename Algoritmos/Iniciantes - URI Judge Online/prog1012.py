valorA , valorB , valorC = [float(i) for i in raw_input().split()]

pi = 3.14159
triangulo_retangulo = ( valorA * valorC ) / 2
circulo  			= pi * valorC**2
trapezio			= ( ( valorA + valorB ) * valorC ) / 2
quadrado			= valorB**2
retangulo 			= valorA * valorB

print 'TRIANGULO: %.3f' %triangulo_retangulo
print 'CIRCULO: %.3f' %circulo
print 'TRAPEZIO: %.3f' %trapezio
print 'QUADRADO: %.3f' %quadrado
print 'RETANGULO: %.3f' %retangulo

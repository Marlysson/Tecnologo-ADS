tempo =       input('Tempo da viagem em horas: ')
veloc_media = input('Velocidade media (km/h): ')

espaco = veloc_media * tempo

litros = espaco / 12.0

print ('Quantidade de litros: %.3f') % litros
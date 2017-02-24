# -*- coding : utf-8 -*-

to_metros = lambda valor : valor / 100.0

altura_pessoa = float(input("Sua altura: "))
sombra_pessoa = float(input("Comprimento da sua sombra ( em cm ): "))

sombra_predio = float(input("Qual a sombra do prédio(em metros): "))

'''
	altura_pessoa -> sombra_pessoa
	altura_predio -> sombra_predio
'''

altura_predio = ( altura_pessoa * sombra_predio ) / to_metros(sombra_pessoa)

print("A altura do prédio é {} metro(s)".format(altura_predio))
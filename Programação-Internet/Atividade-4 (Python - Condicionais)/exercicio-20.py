# -*- coding : utf-8 -*-

# Mostrar mensagem de acordo com o IMC da pessoa

def calcular_imc(altura,massa):
	return massa / float(altura*altura)

def resultado_imc(imc):
	if imc < 18.5:
		return 'Abaixo do peso'
	elif imc < 25:
		return 'Peso normal'
	elif imc < 30:
		return 'Sobrepeso'
	elif imc < 35:
		return 'Obeso leve'
	elif imc < 40:
		return 'Obeso moderado'
	elif imc >= 40:
		return 'Obeso mórbido'

massa = 82
altura = 1.75

imc = calcular_imc(altura,massa)

nivel_imc = resultado_imc(imc)

print("Baseado no seu imc você é : {}".format(nivel_imc))
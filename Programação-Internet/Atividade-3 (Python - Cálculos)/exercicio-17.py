# -*- coding : utf-8 -*-

def to_minutes(hour_minutes_seconds):

	# Rebece a string e faz a separação nos ":"
	# Aplica uma função a todo o elemento da lista retornada anteriormente
	# Faz o casting na função map retornada para retornar lista

	result = list(map(int,hour_minutes_seconds.split(":")))

	hour = result[0]
	minutes = result[1]
	seconds = result[2]

	'''
		Recebendo inteiro
		
		((hour_minutes_seconds // 100) * 60) + hour_minutes_seconds % 100

	'''
	return hour * 60 + minutes + seconds / 60

print(to_minutes("23:45:00"))
tempo_total = input('Quantidade de segundos: ')

horas = tempo_total // 3600
minutos = ( tempo_total - (horas * 60) ) // 60
segundos = tempo_total - (horas * 60) - (minutos * 60)

if segundos > 59:
	minutos += 1
	segundos = segundos - 59
if minutos > 59:
	horas += 1
	minutos = minutos - 59

if len(str(horas)) == 1:
	horas = '0'+str(horas)
if len(str(minutos)) == 1:
	minutos = '0'+str(minutos)
if len(str(segundos)) == 1:
	segundos = '0'+str(segundos)

print '{}:{}:{}'.format(horas,minutos,segundos)

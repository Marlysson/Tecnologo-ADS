# -*- coding : utf-8 -*-

# Recebendo um número e verificando se é múltiplo de um determinado
# is_multiplo(10,2)
# is_multiplo(15,5)

def is_multiplo(multiplo,num):
	if multiplo % num == 0:
		return True
	return False
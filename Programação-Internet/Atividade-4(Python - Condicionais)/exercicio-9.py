# -*- coding : utf-8 -*-
from is_multiplo import is_multiplo
# Retornar booleano dependendo se é multiplo de 5 ou não.

def multiplo_cinco(num):
	return is_multiplo(num,5)

assert multiplo_cinco(5) == True
assert multiplo_cinco(6) == False
assert multiplo_cinco(15) == True
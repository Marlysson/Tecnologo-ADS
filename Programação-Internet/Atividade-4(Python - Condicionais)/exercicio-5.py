# -*- coding : utf-8 -*-

from is_multiplo import is_multiplo

# Retornar booleano se o valor for par

def isPar(num):
	return is_multiplo(num,2)

assert isPar(10) == True
assert isPar(11) == False
assert isPar(12) == True
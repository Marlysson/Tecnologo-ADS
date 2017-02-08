# -*- coding : utf-8 -*-

# Maior de 3

def maior(num1,num2,num3):
	if num1 > num2 and num1 > num3:
		return num1
	elif num2 > num3:
		return num2
	else:
		return num3

assert maior(1,2,3) == 3
assert maior(3,2,1) == 3
assert maior(10,11,12) == 12